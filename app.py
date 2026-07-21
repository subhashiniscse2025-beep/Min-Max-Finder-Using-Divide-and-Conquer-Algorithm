import streamlit as st
import PROGRAM
st.set_page_config(
    page_title="Min-Max Finder",
    page_icon="📊",
    layout="centered"
)
st.title("📊 Min-Max Finder Using Divide and Conquer")
st.write("Compare the Divide and Conquer algorithm with the Naive approach.")
numbers = st.text_input(
    "Enter numbers separated by commas",
    "3,1,7,4,9,2,8,5,6,0"
)
if st.button("Find Min & Max"):
    try:
        arr = [int(x.strip()) for x in numbers.split(",")]
        PROGRAM.comparison_count = 0
        mn, mx = PROGRAM.min_max_dc(arr, 0, len(arr) - 1)
        dc_comps = PROGRAM.comparison_count
        _, _, naive_comps = PROGRAM.min_max_naive(arr)
        st.success(f"✅ Minimum Value: **{mn}**")
        st.success(f"✅ Maximum Value: **{mx}**")
        st.subheader("Comparison Analysis")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Divide & Conquer", dc_comps)
        with col2:
            st.metric("Naive Method", naive_comps)
    except ValueError:
        st.error("Please enter only integers separated by commas.")
st.markdown("---")
st.subheader("Algorithm")
st.markdown("""
### Divide and Conquer Steps
1. Divide the array into two halves.
2. Recursively find the minimum and maximum of each half.
3. Compare the two minimum values.
4. Compare the two maximum values.
5. Return the overall minimum and maximum.

### Time Complexity
- **Divide & Conquer:** O(n)
- **Naive Method:** O(n)

The Divide and Conquer approach performs fewer comparisons (approximately **3n/2 − 2**) than the Naive method (**2(n−1)**).
""")
