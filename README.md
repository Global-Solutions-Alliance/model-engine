# Global Solution Alliance Software Interface

The Global Solutions Alliance (GSA) is an international nonprofit organization (based in the USA) composed of individual and organizational stakeholders aligned around a commitment to collective impact and creating holistic models to inspire and inform action. Through comprehensive, scientific data-driven tools collaboratively designed for use by policy makers, investors, NGOs and other on-the-ground decision-makers, change agents will be able to accelerate their work to solve global warming and secure reliable prosperity for communities in mutually beneficial relationships with the natural environment. 

The founding members of the GSA are Regenerative Intelligence PB LLC, CoLab Cooperative, Buckminster Fuller Institute, The World Fund, The Global Council for Science and the Environment, Grounded, Future Horizon/Future Quest and Sacred Headwaters of the Amazon.

The GSA originated from the recognition that cooperation in a system is integral to creating conditions for life to thrive. Rather than reinventing the wheel, which only stagnates implementation, leads to confusion, and slows progress, the GSA is an evolving ecosystem of partners that are committed to working together in mutually beneficial ways that support the emergence of regenerative economic and social systems. Addressing the global emergencies of warming, climate chaos, ecocide and species extinction requires humanity to move beyond siloed-thinking and work in-parallel towards a future that benefits all. 

Our collective work always begins with rigorous research and analysis to identify the most impactful systemic solutions benefitting people and the planet. The GSA ecosystem of organizations, researchers, and contributors work together to create and maintain a solutions-orientated knowledge commons and accompanying tools hosted on the Solutions Collaboratory (‘Collaboratory’): a free and open source digital public good designed by and for the planet’s solutionists. 

The Collaboratory serves as an open, objective, independent platform and community bringing the best available information and data to the fingertips of global change agents implementing solutions to the climate crisis, biodiversity loss, poverty and hunger, gender inequality, health and well-being, and regenerative economic growth.  

## Status

Conversion Status:
  * Almost all of the solutions (technologies) have been converted.
  * New solutions are converted as they become available
  * Core calculations (used to generate the core results) are completed
  * Most of the "secondary calculations" (which are used to do solution-specific generation of, e.g. emissions factors or adoption estimates) are _not_ yet implemented.
  * The overall integration between multiple solution models (used to model, for example, the impact of adopton of one solution on demand for another) is work in progress.

Other work in progress:
  * Continuing work to make the interfaces more accessible to folks outside the Global Solution Alliance community, both in terms of code improvements and documentation.

For a more detailed list, see the [Issues List](https://github.com/Global-Solutions-Alliance/model-engine/issues).

---
# Using the Model

## Getting the source code


You can [create your own fork of this repository](https://docs.github.com/en/get-started/quickstart/fork-a-repo)
using the `Fork` button at the top of the screen.  From there, follow the instructions to download your fork to your computer.


If you are going to change the code, we recommend immediately making your own branch:
```sh
      $ git checkout -b <your-branch-name-here>
```


## Development Environment

We recommend using [miniconda3](https://docs.conda.io/en/latest/miniconda.html) to create a development environment for this project.
Once miniconda is installed, the following command will create a development environment named `pd-dev` that includes this code, all the
dependencies it requires, and some useful tools such as [pytest](https://pytest.org) and [Jupyter Notebook](https://jupyter-notebook.readthedocs.io/en/stable/)

```sh
      $ conda env create -f environment.yml
      $ conda activate pd-dev
```

A good way to explore the code is to start jupyter notebook

```sh
      $ jupyter notebook
```

then click on `Start_Here.ipynb` to try out a few things.   (Note: the use of jupyter notebook is not a requirement to use the system; use whatever python
development environment is comfortable for you.)

### Minimal Environment

A more minimal environment is available for deployment using [pip](https://pip.pypa.io/en/stable/user_guide/).  This installs this project and its depencies in your current python environment, but no extra tools:

```sh
      $ pip install -r requirements.txt
```

Python 3.9 is required.


### Using GSA Model Engine as a package

If you would like to use this project as a dependency in _your_ code, you can do so by including the following line in your requirements.txt file:

```
      git+git://github.com/Global-Solutions-Alliance/model-engine@develop
```


## Documentation

The main code documentation can be found at the [Documentation](https://github.com/Global-Solutions-Alliance/model-engine/tree/develop/Documentation) folder.

---

## License

The python code for the collaboratory is licensed under the GNU Affero General Public license and subject to the license terms in the LICENSE file. No part of this Project, including this file, may be copied, modified, propagated, or distributed except according to the terms contained in the LICENSE file.

Data supplied (mostly in the form of CSV files) is licensed under the [CC-BY-NC-2.0](https://creativecommons.org/licenses/by-nc/2.0/) license for non-commercial use. The code for the model can be used (under the terms of the AGPL) to process whatever other data the user wishes under whatever license those data carry.

---

## Support
Please use the [Issues List](https://github.com/Global-Solutions-Alliance/model-engine/issues) to report any bugs you find, or ask any
questions you have.


## Contributing
We would love to have your help.
Please see [CONTRIBUTING.md](https://github.com/Global-Solutions-Alliance/model-engine/blob/develop/CONTRIBUTING.md) for guidelines for contributing to this project.

## Acknowledgements

The initial versions of these repos were ported from those of Project Drawdown, which are in the public domain.

## Contact

CoLab Cooperative (gsa@colab.coop) is currently the technical point of contact for this project.

