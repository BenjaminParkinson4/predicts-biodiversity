---
marp: true
theme: default
paginate: false
backgroundColor: white
style: |
  @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css');
  img[alt~="center"] {
    display: block;
    margin: 0 auto;
  }
  section.invert {
    text-align: center;
  }
  footer {
    text-align: right;
    right: 100px;
  }
  section {
    padding: 30px; /* Removes all padding */
    /* Or set specific padding values, e.g., padding: 10px; */
  }
---

# MM-BioGraph: Multimodal Data Analysis for Link Prediction in Biodiversity Graphs

<style scoped>section{ font-size: 120%}</style>

<div style="display: grid; grid-template-columns: 0.8fr 1fr;repeat(2, minmax(0, 1fr));">

<div>

![w:200 h:150](assets/image-6.png) ![h:200](https://onlinelibrary.wiley.com/cms/asset/4aff7b84-5a0b-49f0-ad45-44109e710e45/ece32579-fig-0006-m.jpg)

## Context

- **Biodiversity Intactness Index (BII):** Quantifies the impact of human activities on biodiversity by assessing changes in species abundance across various biomes (PREDICTS dataset).
- **Problem:** Valuable multimodal biodiversity data (text reports, images) are often siloed, hindering comprehensive understanding of relationships.
  - Can land-use data and images reveal environmental impacts on BII and species changes?
- There is a partnership with a Researcher from National History Museum (NHM) Future Lab, who created the PREDICTS Dataset

</div>

<div>

![h:200 w:280](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fspotintelligence.com%2Fwp-content%2Fuploads%2F2024%2F01%2Flink-prediction-graphical-neural-network.jpg&f=1&nofb=1&ipt=cc13f08c1153a7d5ec2e56cd652a8920590b9413c6f80b3062e5a5ad88881c38) ![h:180 w:180](assets/image.png) ![h:180 w:180](assets/image-1.png)

## Methodology

The project aims to integrate diverse data into graph-based structures to represent biodiversity relationships and predict unobserved links.

1. **BII Multimodal Dataset Generation**: Collaborate with NHM specialists to develop a comprehensive multimodal dataset (textual, visual, ecological) to support robust graph representation.
2. **GNN Baseline Development**: Establish a **Graph Neural Network (GNN) baseline model** for initial analysis of biodiversity relationships using the generated dataset.
3. **LLM-Assisted GNN**: Build upon the GNN baseline by applying **Large Language Models (LLMs)** alongside visual data. This approach will iteratively refine predictions and achieve more accurate and comprehensive insights into complex biodiversity relationships. It can also leveraging **Chains of Thought (CoT)** reasoning.

</div>
</div>

---

## References

- https://www.nhm.ac.uk/our-science/services/data/biodiversity-intactness-index.html
- https://onlinelibrary.wiley.com/doi/full/10.1002/ece3.2579
- https://dl.acm.org/doi/abs/10.1145/3581783.3612266
- https://arxiv.org/abs/2403.07311

Datasets:

- https://data.nhm.ac.uk/dataset/release-of-data-added-to-the-predicts-database-november-2022
- https://data.nhm.ac.uk/dataset/the-2016-release-of-the-predicts-database
- https://data.nhm.ac.uk/dataset/bii-developed-by-nhm-v2-1-1-limited-release
