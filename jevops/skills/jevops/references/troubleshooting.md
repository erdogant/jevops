# Troubleshooting

<!--
AGENT INSTRUCTIONS

Complete this troubleshooting guide for the target repository.

Before editing this file:

1. Inspect the repository structure.
2. Read the README and documentation.
3. Inspect the package dependencies and supported Python versions.
4. Inspect the public API and examples.
5. Inspect the tests for known edge cases and expected behavior.
6. Look for common issues in:
   - installation
   - imports
   - dependencies
   - API usage
   - input data
   - parameters
   - runtime errors
   - performance
   - reproducibility
   - platform compatibility
7. Search existing issues, documentation, or changelogs when available.
8. Replace generic examples with real commands and API calls from the repository.

IMPORTANT:
- Replace `jevops` with the actual package/repository name.
- Do not invent problems, error messages, APIs, parameters, or solutions.
- Keep only troubleshooting sections that are relevant to the library.
- Add library-specific problems discovered during repository inspection.
- Prefer concrete solutions and minimal reproducible examples.
- Use the actual package name, import name, and API.
- Make sure all code examples are valid for the current version of the library.
- Remove this instruction block from the final completed troubleshooting guide.
-->

Use this guide to diagnose and resolve common issues when working with **jevops**.

## Installation issues

<!--
AGENT: Document actual installation requirements and common installation failures.

Check:
- Python version requirements
- operating-system requirements
- package installation name
- optional dependencies
- system dependencies
- dependency conflicts
- development installation
-->

### Package cannot be installed

<!--
AGENT: Replace this section with repository-specific installation problems.

Explain:
- what commonly causes the installation failure
- how to diagnose it
- the recommended solution
-->

Verify the environment with:

```bash
python --version
python -m pip --version
python -m pip show jevops
```

<!--
AGENT: Replace the following command if the package uses a different
installation method.
-->

```bash
python -m pip install -U jevops
```

### ImportError or ModuleNotFoundError

<!--
AGENT: Document actual import problems encountered with the library.

Use the real Python import name, which may differ from the PyPI package name.
-->

If Python cannot import the library or one of its dependencies:

1. Confirm that the package is installed in the active environment.
2. Check that the Python interpreter used to run the script is the same one where the package was installed.
3. Check the dependency versions.
4. Restart the Python session after changing the environment.

Example:

```bash
python -c "import jevops; print(jevops.__version__)"
```

---

## API issues

<!--
AGENT: Add common API-related errors discovered from the repository,
tests, documentation, or known compatibility issues.
-->

### Function or class not found

<!--
AGENT: Document real functions/classes that commonly cause confusion.

Explain:
- correct import path
- whether the API is public
- version-specific differences
- deprecated or renamed APIs
-->

If an API cannot be found:

* Check the installed library version.
* Verify the import path.
* Check whether the API has been renamed, moved, or deprecated.
* Consult the documentation for the installed version.

### Unexpected argument or keyword argument

<!--
AGENT: Add actual examples of incorrect arguments if known.
-->

An error such as:

```text
TypeError: ... got an unexpected keyword argument ...
```

usually indicates that:

* The argument name is incorrect.
* The argument was removed or renamed.
* The installed library version differs from the documentation or example.
* A different function than expected is being called.

Inspect the function signature:

```python
import inspect

print(inspect.signature(jevops.some_function))
```

<!--
AGENT: Replace `some_function` with a real function or remove this example.
-->

---

## Data issues

<!--
AGENT: Determine whether the library has specific input-data requirements.

Document:
- accepted input types
- required columns
- required dtypes
- missing-value handling
- categorical requirements
- numerical requirements
- shape requirements
- indexing requirements
-->

### Unexpected results

When the library produces unexpected results, first verify the input data.

Check:

* Data types.
* Missing values.
* Duplicate observations.
* Unexpected categorical values.
* Numeric ranges.
* Number of observations.
* Column names.
* Index values.
* Whether preprocessing was applied as expected.

For pandas data:

```python
print(df.shape)
print(df.dtypes)
print(df.isna().sum())
print(df.describe(include="all"))
```

<!--
AGENT: Keep this section only if pandas is relevant to the library.
Replace it with the appropriate input-validation code otherwise.
-->

### Results contain NaN or infinite values

<!--
AGENT: Determine whether NaN/inf values are actually problematic for the library.
Explain the supported handling strategy rather than recommending arbitrary
imputation or replacement.
-->

Check for missing or infinite values before passing data to the library:

```python
import numpy as np

print(df.isna().sum())
print(np.isinf(df.select_dtypes(include="number")).sum())
```

Handle invalid values according to the requirements of the specific algorithm rather than automatically replacing them.

---

## Parameter issues

<!--
AGENT: Add this section if the library has important parameters that commonly
cause unexpected behavior.

For each important parameter:
- explain valid values
- explain common mistakes
- explain interactions with other parameters
- provide a recommended example
-->

### Invalid parameter combinations

<!--
AGENT: Document real incompatible parameter combinations here.
-->

**Problem:** Describe the error or unexpected behavior.

**Cause:** Explain why the parameters are incompatible.

**Solution:** Show the correct configuration.

```python
# Minimal valid example.
```

---

## Performance issues

<!--
AGENT: Document actual performance characteristics of the library.

Identify:
- computationally expensive operations
- memory-intensive operations
- parallelization support
- recommended parameters
- scalability limitations
-->

### The operation is slow

When performance is unexpectedly poor:

1. Check the size of the input data.
2. Check the algorithm and its computational complexity.
3. Reduce unnecessary preprocessing or repeated computations.
4. Check whether parallel processing is supported.
5. Profile the expensive part of the workflow.

For Python code:

```python
import time

start = time.perf_counter()

# operation

print(f"Elapsed time: {time.perf_counter() - start:.2f}s")
```

### Memory usage is too high

<!--
AGENT: Keep this section if memory usage is relevant.
Add library-specific recommendations.
-->

Large datasets or intermediate objects can consume substantial memory.

Check:

```python
print(df.memory_usage(deep=True).sum() / 1024**2, "MB")
```

Consider:

* Reducing unnecessary columns.
* Using appropriate data types.
* Processing data in batches.
* Avoiding unnecessary copies.
* Reducing intermediate objects.
* Using a smaller dataset to reproduce the problem.

---

## Reproducibility

<!--
AGENT: Determine whether the library contains stochastic algorithms.

If it does, document:
- random_state/random_seed parameters
- sources of randomness
- deterministic settings
- parallel-processing considerations
-->

If results differ between runs, check:

* Random seeds.
* Library versions.
* Python version.
* Input data ordering.
* Parallel execution.
* Numerical precision.
* Hardware-specific behavior.

When supported, explicitly set a random seed:

```python
random_state = 42
```

Record the environment when reporting a problem:

```bash
python --version
python -m pip show jevops
```

---

## Platform and dependency compatibility

<!--
AGENT: Add platform-specific issues discovered in the repository.

Examples:
- Windows-specific issues
- Linux system libraries
- macOS compatibility
- NumPy/SciPy compatibility
- Python-version compatibility
- GPU/CUDA requirements
-->

### Dependency conflict

**Problem:** Describe the dependency conflict.

**Cause:** Identify the incompatible versions or packages.

**Solution:** Provide the supported versions or installation procedure.

```bash
# Actual installation command.
```

---

## Debugging workflow

<!--
AGENT: Keep and adapt this workflow to the library.
Add repository-specific debugging commands when useful.
-->

When troubleshooting a problem, reduce it to the smallest reproducible example.

A useful debugging workflow is:

1. Reproduce the error.
2. Capture the complete error message and traceback.
3. Check the library and Python versions.
4. Verify the input data.
5. Reduce the example to the smallest failing case.
6. Test the relevant API independently.
7. Check the documentation for the installed version.
8. Determine whether the problem is caused by the library, dependencies, environment, or input data.

A good bug report should include:

* Python version.
* Operating system.
* Library version.
* Relevant dependency versions.
* Minimal reproducible example.
* Input data or a representative sample.
* Complete traceback.
* Expected behavior.
* Actual behavior.

---

## Common pitfalls

<!--
AGENT: Replace these generic examples with actual pitfalls discovered from
the repository, documentation, examples, and tests.

Remove this section if no meaningful library-specific pitfalls exist.
-->

* Using an API from a different library version.
* Passing data in an unsupported format.
* Using incompatible parameter combinations.
* Forgetting required preprocessing.
* Assuming deterministic output from a stochastic algorithm.
* Ignoring warnings that indicate deprecated functionality.

---

## Library-specific troubleshooting

<!--
AGENT: This should be the most valuable section of the completed file.

Add one subsection for each important real-world problem.

Prioritize problems that:
- occur frequently
- are difficult to diagnose
- produce misleading errors
- depend on library-specific behavior
- are not obvious from the API documentation
-->

### Problem

**Symptom:** Describe exactly what the user observes.

**Cause:** Explain the underlying cause.

**Solution:** Provide the recommended solution.

**Example:**

```python
# Minimal reproducible example or solution.
```

### Problem

**Symptom:** Describe the observed behavior.

**Cause:** Explain the cause.

**Solution:** Provide the recommended solution.

**Example:**

```python
# Minimal reproducible example or solution.
```

---

## Version-specific issues

<!--
AGENT: Add this section only if behavior differs significantly between versions.

Document:
- deprecated APIs
- renamed parameters
- changed defaults
- dependency compatibility
- migration instructions
-->

### Version X → Version Y

**Changed:** Describe the change.

**Impact:** Explain who is affected.

**Migration:** Show how to update existing code.

```python
# Before

# After
```

---

## Final validation

<!--
AGENT:

Before considering this troubleshooting guide complete:

1. Search for remaining `jevops` placeholders.
2. Search for `TODO` markers.
3. Search for `some_function` and other placeholder API names.
4. Verify every command uses the correct package name.
5. Verify every import uses the correct Python module name.
6. Verify every code example against the current API.
7. Remove sections that are not relevant.
8. Ensure all important known issues are documented.
9. Ensure referenced examples and files actually exist.
10. Run the examples where possible.
-->
