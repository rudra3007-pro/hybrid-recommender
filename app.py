import streamlit as st
import pandas as pd
from data_adapter import adapt_data
from content_model import ContentRecommender
from collaborative_model import CollaborativeRecommender
from hybrid_model import HybridRecommender

st.title("📊 Hybrid Recommender System")
if "recently_viewed" not in st.session_state:
    st.session_state.recently_viewed = []

uploaded_file = st.file_uploader("Upload your dataset (CSV)")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.write("### Raw Data")
    st.dataframe(df.head())

    # Apply Data Adapter
    adapted_df, meta = adapt_data(df)

    st.write("### Detected Columns")
    st.json(meta)

    st.write("### Adapted Data")
    st.dataframe(adapted_df.head())

    # Build models
    content_model = ContentRecommender(adapted_df)

    collab_model = None
    if meta['has_user_data']:
        collab_model = CollaborativeRecommender(adapted_df)

    hybrid_model = HybridRecommender(content_model, collab_model)

    item_list = adapted_df['title'].dropna().unique()
    # Limit selectbox options to prevent browser OOM with huge datasets
    if len(item_list) > 100:
        item_list = item_list[:100]
    selected_item = st.selectbox("Select Item", item_list)

   
    if st.button("Recommend"):

    # Add selected item to recently viewed
        if selected_item in st.session_state.recently_viewed:
            st.session_state.recently_viewed.remove(selected_item)

        st.session_state.recently_viewed.insert(0, selected_item)

    # Keep only last 10 items
        st.session_state.recently_viewed = \
            st.session_state.recently_viewed[:10]

        st.write(recs)
        recs = hybrid_model.recommend(selected_item)
        st.write("### Recommendations")
        st.write(recs)
    st.write("## Recently Viewed Products")

if st.session_state.recently_viewed:

    cols = st.columns(
        min(len(st.session_state.recently_viewed), 5)
    )

    for idx, item in enumerate(
        st.session_state.recently_viewed[:5]
    ):
        with cols[idx]:
            st.info(item)

    if st.button("Clear History"):
        st.session_state.recently_viewed = []
        st.rerun()

else:
    st.write("No recently viewed products.")