# How to manage environments in Julia
Julia's counterpart to Python-`environments` are `Projects`. This tutorial is based on [this one](https://towardsdatascience.com/how-to-setup-project-environments-in-julia-ec8ae73afe9c).

## Clean base environment
First of all, make sure that your base environment is clean.
```bash
julia
```
Go into package-mode and check the status of your environment (currently the base environment named `@v1.9`)
```julia
]
(@v1.9) pkg> status
```
By `remove <PackageName>` you can now remove packages until `status` displays `(empty project)`, e.g.,
```julia
(@v1.9) pkg> remove LinearAlgebra
```

## Generate and fill a new environment
Create a new environment called `NewProject`` by
```Julia
(@v1.9) pkg> generate NewProject
```
which creates a base .jl-File for your modules along with a Project.toml file (both in a new directory called _NewProject_).
Now  activate your new baby and check the status
```Julia
(@v1.9) pkg> activate NewProject

(NewProject) pkg> status
```
You can now add Packages easily
```Julia
(NewProject) pkg> add LinearAlgebra
```
which automatically creates a `Manifest.toml` where all dependencies are listed. `Project.toml` should now only mention _LinearAlgebra_ if you check for the status. You can add specific versions of packages using
```Julia
(NewProject) pkg> add IJulia@1.24.2
```
To update all packages in our project environment, use the `update` command. In the same way you can remove packages by using the `remove` command, which you have used already above.

Starting julia with a specific Project can be done by
```bash
julia --project=NewProject
```