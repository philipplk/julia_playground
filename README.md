# Julia Playground

## References
- [Getting started](https://docs.julialang.org/en/v1/manual/getting-started/)
- [Differences to Python](https://docs.julialang.org/en/v1/manual/noteworthy-differences/#Noteworthy-differences-from-Python)
- [Differences to Matlab][https://docs.julialang.org/en/v1/manual/noteworthy-differences/#Noteworthy-differences-from-MATLAB]
- [Developing Packages](https://julialang.org/contribute/developing_package/)
- [Pkg docs](https://pkgdocs.julialang.org/v1/managing-packages/#Adding-unregistered-packages)
- [Pkg environments](https://pkgdocs.julialang.org/v1/environments/)

## Install / add / dev the new local package

Enter "package-mode" in Julia-session terminal by pressing `]` then type
```bash
dev ./Package1/
```

after that, use the package by

```julia
import Package1
```

## Remove package from current environment

```
pkg> rm Package1
```


## Installation

### MacOS

Follow the instructions on the official [Julia](https://julialang.org/downloads/platform/) webpage.

### Ubuntu
Download and extract binary files from [here](https://julialang.org/downloads/platform/#linux_and_freebsd).

### Make Julia accesible in shell

Include julia binary in system path, e.g., 
```bash
# julia
export PATH="/home/julian/git/julia/julia-1.9.4/bin:$PATH"
```

## Next steps
- Environments
- Equivalents to
    - `numpy`
    - `numpy.ndarray`
    - `numpy.einsum`
    - `pandas`
    - `matplotlib`
- Matlab-to-Julia converter
- Minimal working example