# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to Semantic Versioning principles where applicable.

---

## [Unreleased]

### Added

* Dynamic contributors section in `README.md`
* Contributor avatar grid using `contrib.rocks`
* Language identifiers for all README code blocks
* Improved README formatting and setup documentation

### Changed

* Updated markdown code fences for GitHub copy-button support
* Improved Quick Start formatting and readability

---

## [2026.1.0] - GSSoC 2026

### Added

* GSSoC 2026 contribution workflow improvements
* GitHub issue templates and PR templates
* Assignment bot integration
* Pull request automation bot integration
* GitHub Actions CI workflows
* Automated repository health checks
* `tests/` directory for backend and pipeline validation
* `data_preprocessing.py` for dataset cleaning and normalization

### Changed

* Enhanced contributor onboarding documentation
* Improved repository structure and developer experience
* Updated README with contribution guidelines and architecture details

### Fixed

* Markdown formatting inconsistencies
* README code block rendering issues
* Documentation clarity improvements

---

## [2025.1.0] - Initial Release

### Added

* Hybrid recommender system architecture
* TF-IDF content-based recommendation engine
* Collaborative filtering using Truncated SVD
* NLP sentiment analysis using VADER
* Supabase PostgreSQL integration
* FastAPI backend APIs
* Full-text search with PostgreSQL FTS
* Dataset upload and model-building pipeline
* Cold-start recommendation handling
* Responsive frontend interface
* Evaluation metrics pipeline (`Precision@K`, `Recall@K`, `NDCG@K`)
* Secure authentication and Row-Level Security support

### Changed

* Iterative tuning of hybrid recommendation weights
* Improved recommendation ranking logic

### Fixed

* Sparse matrix dimensionality handling in collaborative filtering
* Search performance optimizations
