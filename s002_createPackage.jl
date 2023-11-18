using Pkg
Pkg.add("PkgTemplates")

using PkgTemplates

t = Template(;
    user="philipplk",
    authors=["Philipp Kinon", "Julian Karl Bauer"],
    plugins=[
        License(name="MIT"),
        Git(),
        GitHubActions(),
    ],
)

t("Package1")