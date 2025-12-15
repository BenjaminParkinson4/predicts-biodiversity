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

<!-- _class: invert -->
<!-- _backgroundColor: #46afa0 -->
<!-- _paginate: skip -->

<img src="assets/base/cs_logo.png" width="600"/>

# MM-BioGraph: Multimodal Data Analysis for Link Prediction in Biodiversity Graphs

---

# Agenda

- Problem defintion
- Initial results
- Data exploration and questions
- Next steps

---

# Problem definition

---

# Tabular data problem

<div style="text-align: center;">
<br>
<br>

$Prediction(\mathcal{X}) = \mathcal{Y}_x$

</div>

- $\mathcal{X}$: Specie observation over a region
  - $S$ (species), $L$ land usage, $B$ biome type, ...
- $\mathcal{Y}_xt$: Predicted species $S$

---

# Tabular data problem

## Who does this:

- Adriana method
- Alan MSc Student
- Others academics using predicts

What is usefull for:
<!-- TODO -->

---

# Time-based problem

<div style="text-align: center;">
<br>
<br>

$TimeBasedPrediction(\mathcal{X}_{pw}) = \mathcal{Y}_fw$

</div>

- $\mathcal{pw}$: Specie observation over  a region during a time window $pw$: $S_t$ (species), $L$ land usage, $B$ biome type
- $\mathcal{X}$: Specie observation over a region, $S$ (species), $L$ land usage, $B$ biome type
- $\mathcal{Y}_xt$: Predicted species $S$

---

# Time-based problem

## Who does this:

- Adriana method
- Alan MSc Student
- Others academics using predicts

What is usefull for:
<!-- TODO -->
---

# Time-based problem

Who does this:

-

What is usefull for:
<!-- TODO -->
---

<!-- _class: invert -->
<!-- _backgroundColor: #46afa0 -->
<!-- _paginate: skip -->

# Data exploration

---

# Feature importance

---

# Questions

- Which are more important features for the prediction?
  - They differ from the tabular to the time-base?
- <!-- TODO  -->

---

<!-- _class: invert -->
<!-- _backgroundColor: #46afa0 -->
<!-- _paginate: skip -->

# Next steps

---

# Next steps

- MC1 February
- XX: time-based baseline
- XX: Graph-time-based baseline
