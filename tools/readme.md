# Benchmark Modification Guide

This document provides guidelines on how to modify benchmarks for your needs. There are two main parts you might want to modify: prompts and metrics.

## Modifying Prompts

1. **Locate and Modify the Prompt File:**
   - Navigate to the `prompt` folder.
   - Find the `.txt` file containing the prompts.
   - Make necessary changes to this file.

2. **Regenerate Files:**
   - Use the three scripts provided in the same folder to regenerate the ground truth files and the weight file.

3. **Update Files:**
   - Modify the newly generated ground truth and weight files according to your statistics.
   - Replace the original files with the modified versions.

## Modifying Metrics

1. **Modify Files for Metrics:**
   - If you are only interested in modifying the metric, start by modifying the ground truth files and the weight file found in the `truth` folder.
   - Update these files as per your collected statistics.

Please ensure all modified files are correctly placed in their respective directories to avoid any discrepancies in benchmark performance.
