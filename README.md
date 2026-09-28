# Machine Learning Internship @ Skill Set Go EduTech

4 week Machine Learning internship (Sep 2026 to Oct 2026): Python and data fundamentals →
deep learning with PyTorch → TensorFlow and generative AI → LangChain agents.

**Author:** Imangali Bayangaliyev ([GitHub](https://github.com/peemoshi))

## Tech Stack

Python · pandas · NumPy · scikit-learn · PyTorch · pytest · (Week 3–4: TensorFlow, LangChain, LangGraph)

## Highlights so far

- Built and tested 8 core Python modules (variables, loops, functions, OOP, file I/O, exceptions)
  behind a 63-test pytest suite — all passing.
- Cleaned and explored the UCI Student Performance dataset, uncovering a counterintuitive finding:
  students with extra educational support performed *worse* on average — most likely reverse
  causation (support is targeted at already-struggling students) rather than support being harmful.
- Trained a feedforward neural network in PyTorch on the UCI Adult Income dataset, reaching **86.3%
  test accuracy** against a 76% majority-class baseline.
- Built a CNN for CIFAR-10 image classification, reaching **72.7% test accuracy** (baseline: 10%
  random guess for 10 classes); confusion matrix showed the model separates broad categories
  reliably but struggles most on cats vs. dogs.
- Ran a controlled hyperparameter comparison on the CNN, isolating one variable at a time —
  learning rate and optimizer choice moved accuracy by 12–15 points, batch size by under 1 point.

## Progress

| Week | Focus | Status |
|---|---|---|
| 1 | Python fundamentals, data cleaning & EDA, math for ML, scikit-learn models | ✅ Done |
| 2 | Deep learning with PyTorch (NN, CNN, hyperparameter tuning, technical report) | ✅ Done |
| 3 | TensorFlow, GenAI & prompt engineering | ⏳ Not started |
| 4 | LangChain, LangGraph & AI agent capstone | ⏳ Not started |

## Weekly breakdown

### Week 1 — Foundations

- [`1.1 Python fundamentals`](week-1/1.1-python-fundamentals) — 8 topic exercises (conditions/loops,
  functions, collections, file I/O, exceptions, OOP) culminating in a mini gradebook project that
  reuses earlier functions. Verified with a 63-test pytest suite.
- [`1.2 Data cleaning & EDA`](week-1/1.2-data-cleaning-eda) — cleaned the UCI Student Performance
  dataset and investigated grade distribution, study time, alcohol use, and absences. The most
  interesting result: students receiving extra school support had lower average grades; explained
  as reverse causation rather than the support itself being unhelpful.
- [`1.3 Math for ML`](week-1/1.3-math-for-ml) — 11 worked problems spanning descriptive statistics,
  Bayes' rule, linear algebra (dot products, matrix multiplication), and gradient descent, solved by
  hand and cross-checked in NumPy.
- [`1.4 Scikit-learn models`](week-1/1.4-scikit-learn-models) — regression and classification on the
  cleaned student dataset, each compared against a dummy baseline to confirm the models learned real
  signal rather than trivial patterns; G1/G2 grades excluded from features to avoid data leakage.

### Week 2 — Deep Learning with PyTorch

- [`2.1 Neural network`](week-2/2.1-neural-network-pytorch) — feedforward network on the UCI Adult
  Income dataset predicting income >$50K. Reached 86.3% test accuracy vs. a 76% majority-class
  baseline, with mild overfitting after epoch 8.
- [`2.2 CNN image classifier`](week-2/2.2-cnn-image-classifier) — convolutional network on CIFAR-10.
  Reached 72.7% test accuracy vs. a 10% random-guess baseline; error analysis via confusion matrix
  showed cats vs. dogs as the main weak point.
- [`2.3 Hyperparameter experiments`](week-2/2.3-hyperparameter-experiments) — four training runs on
  the same CNN, changing one hyperparameter at a time (learning rate, optimizer, batch size) against
  a shared baseline, to isolate what actually drives performance.
- [`2.4 Technical report`](week-2/2.4-deep-learning-report) — a 2-page PDF report comparing all three
  Week 2 experiments: problem statement, architecture summary, results table, and an explicit
  over/underfitting analysis with limitations and next steps.

### Week 3 — TensorFlow, GenAI & Prompt Engineering *(not started)*

### Week 4 — LangChain, LangGraph & AI Agent Capstone *(not started)*

## Repository structure

```
ai-ml-internship/
├── week-1/
│   ├── 1.1-python-fundamentals/
│   │   └── tests/
│   ├── 1.2-data-cleaning-eda/
│   ├── 1.3-math-for-ml/
│   └── 1.4-scikit-learn-models/
├── week-2/
│   ├── 2.1-neural-network-pytorch/
│   ├── 2.2-cnn-image-classifier/
│   ├── 2.3-hyperparameter-experiments/
│   └── 2.4-deep-learning-report/
├── requirements.txt
└── README.md
```

## Setup

```bash
git clone https://github.com/peemoshi/ai-ml-internship.git
cd ai-ml-internship
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Run the Week 1 test suite:

```bash
pytest week-1/1.1-python-fundamentals/tests -v
```

Notebooks (`.ipynb`) are designed to run in Google Colab — open directly from the
`week-*` folders above.
