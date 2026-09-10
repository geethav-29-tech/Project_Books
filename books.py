import streamlit as st
import pandas as pd
from PIL import Image

# ---------------------------------------------------------
# Page configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="Book Store",
    page_icon="📚",
    layout="wide"
)

# ---------------------------------------------------------
# Load dataset
# ---------------------------------------------------------
df = pd.read_csv(r"books_data_with_all_20pages.csv")

# ---------------------------------------------------------
# Page title
# ---------------------------------------------------------
st.title("📚 Book Store")
st.write("Browse our collection of books")

# ---------------------------------------------------------
# Pagination settings
# ---------------------------------------------------------
books_per_page = 20

# Number of pages
total_pages = (len(df) + books_per_page - 1) // books_per_page

# Create page number
if "page" not in st.session_state:
    st.session_state.page = 1

# ---------------------------------------------------------
# Get books for current page
# ---------------------------------------------------------
start = (st.session_state.page - 1) * books_per_page
end = start + books_per_page

page_df = df.iloc[start:end]

# ---------------------------------------------------------
# Display books
# 4 books in each row
# ---------------------------------------------------------

for row_start in range(0, len(page_df), 4):

    row = page_df.iloc[row_start:row_start + 4]

    columns = st.columns(4)

    for col, (_, book) in zip(columns, row.iterrows()):

        with col:

            # Book image
            st.image(
                book["image_url"],width=200,
                use_container_width=True
            )

            # # Open the image file
            # image = Image.open(book["image_url"])
            # # Force an exact width and height (ignoring aspect ratio)
            # resized_image = image.resize((400, 300))
            # # Display the modified image object
            # st.image(resized_image,use_container_width=True)

            # Book title
            st.subheader(book["title"])

            # Price
            st.write(f"💰 **Price:** £{book['price']}")

            # Rating
            st.write(f"⭐ **Rating:** {book['rating']}")

            # Availability
            st.write(f"📦 **{book['stock availability']}**")

            st.divider()


# ---------------------------------------------------------
# Pagination buttons
# ---------------------------------------------------------

st.write("")

col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button("⬅️ Previous"):
        if st.session_state.page > 1:
            st.session_state.page -= 1
            st.rerun()

with col2:
    st.markdown(
        f"<h4 style='text-align: center;'>"
        f"Page {st.session_state.page} of {total_pages}"
        f"</h4>",
        unsafe_allow_html=True
    )

with col3:
    if st.button("Next ➡️"):
        if st.session_state.page < total_pages:
            st.session_state.page += 1
            st.rerun()