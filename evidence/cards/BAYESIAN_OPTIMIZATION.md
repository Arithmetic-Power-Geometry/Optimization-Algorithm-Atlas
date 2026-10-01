# Bayesian Optimization Evidence Card

## Core mechanism
Bayesian optimization uses a probabilistic surrogate plus an acquisition rule to choose expensive evaluations.

## Main evidence boundary
Its sample efficiency is attractive for expensive black-box objectives, but standard surrogate modeling and acquisition optimization become difficult in high-dimensional spaces. High-dimensional BO methods commonly introduce structural assumptions such as effective low dimension, additivity, embeddings, sparsity, or locality.

## Mechanism question
When does the sample-efficiency advantage disappear because the surrogate's structural assumption is wrong or because model/acquisition overhead dominates?

## Candidate test
Compare BO families under controlled intrinsic-vs-ambient dimension, interaction strength, evaluation cost, noise and budget. Report both objective evaluations and total decision time.

Status: candidate; this is an assumption-failure question rather than a universal BO weakness.
