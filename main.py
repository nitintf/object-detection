import streamlit as st
import cv2
import numpy as np
from streamlit_config import init_app
from ultralytics import YOLO
import supervision as sv

# Initialize app configuration and styles
init_app()

st.title("Advanced Object Segmentation App")
st.markdown("---")

# Sidebar configuration
with st.sidebar:
    st.header("️Configuration")
    confidence_threshold = st.slider(
        "Confidence Threshold", min_value=0.0, max_value=1.0, value=0.3, step=0.05
    )
    show_confidence = st.checkbox("Show Confidence Scores", value=True)


@st.cache_resource
def load_model():
    return YOLO("yolov8n-seg.pt")


model = load_model()

files = st.file_uploader(
    "Upload images", type=["jpg", "jpeg", "png"], accept_multiple_files=True
)

if files:
    progress_bar = st.progress(0)

    # Process all images first
    processed_results = []
    class_names = model.names
    box_annotator = sv.BoxAnnotator(thickness=2)
    label_annotator = sv.LabelAnnotator(text_thickness=1, text_scale=0.5)

    for idx, file in enumerate(files):
        progress = (idx + 1) / len(files)
        progress_bar.progress(progress)

        # Convert file to bytes
        file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
        image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Store original image (make a copy to ensure it's not modified)
        original_image = image_rgb.copy()

        # Perform prediction
        results = model.predict(image_rgb, conf=confidence_threshold)
        result = results[0]

        # Get detections
        detections = sv.Detections(
            xyxy=result.boxes.xyxy.cpu().numpy(),
            confidence=result.boxes.conf.cpu().numpy(),
            class_id=result.boxes.cls.cpu().numpy().astype(int),
        )

        # Create labels with class names and confidence scores
        if show_confidence:
            labels = [
                f"{class_names[class_id]} {confidence:.2f}"
                for class_id, confidence in zip(
                    detections.class_id, detections.confidence
                )
            ]
        else:
            labels = [f"{class_names[class_id]}" for class_id in detections.class_id]

        # Annotate image (create a copy for annotation)
        image_for_annotation = image_rgb.copy()
        boxes = box_annotator.annotate(
            scene=image_for_annotation, detections=detections
        )
        annotated_image = label_annotator.annotate(
            scene=boxes, detections=detections, labels=labels
        )

        # Store results
        detected_classes = [class_names[class_id] for class_id in detections.class_id]
        processed_results.append(
            {
                "original": original_image,
                "processed": annotated_image,
                "detections": detections,
                "detected_classes": detected_classes,
                "index": idx + 1,
            }
        )

    progress_bar.empty()

    # Display images in rows of 3
    for row_start in range(0, len(processed_results), 3):
        row_results = processed_results[row_start : row_start + 3]
        cols = st.columns(3)

        for col_idx, result in enumerate(row_results):
            with cols[col_idx]:
                st.subheader(f"Image {result['index']}")

                # Tabs for Original and Processed views
                tab1, tab2 = st.tabs(["🖼️ Original", "✨ Processed"])

                with tab1:
                    st.image(result["original"], use_container_width=True)

                with tab2:
                    st.image(result["processed"], use_container_width=True)

                # Display detection summary
                detections = result["detections"]
                detected_classes = result["detected_classes"]

                if len(detections) > 0:
                    detected_classes_str = ", ".join(detected_classes)

                    # Statistics
                    st.metric("Detections", len(detections))
                    unique_classes = len(set(detected_classes))
                    avg_confidence = (
                        np.mean(detections.confidence) if len(detections) > 0 else 0
                    )

                    st.caption(
                        f"**Classes:** {unique_classes} | **Conf:** {avg_confidence:.2f}"
                    )
                    st.caption(f"**Detected:** {detected_classes_str}")
                else:
                    st.info("No objects detected")

        st.divider()
else:
    st.info("👆 Please upload one or more images to get started.")
