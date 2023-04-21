<meta http-equiv="refresh" content="0; url='https://mimbcd-ui.github.io/dataset-uta11-findings/web/index.html'" />

# UTA11: Findings Dataset

<img src="https://github.com/MIMBCD-UI/meta/blob/master/banners/datasets_1280x640.png?raw=true" width="100%" />

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg?style=flat-square)](https://github.com/MIMBCD-UI/dataset-uta11-findings/blob/master/LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/MIMBCD-UI/dataset-uta11-findings?style=flat-square)](https://github.com/MIMBCD-UI/dataset-uta11-findings/commits/master)
[![OpenCollective](https://opencollective.com/oppr/backers/badge.svg?style=flat-square)](#backers)
[![OpenCollective](https://opencollective.com/oppr/sponsors/badge.svg?style=flat-square)](#sponsors)
[![Gitter](https://img.shields.io/gitter/room/gitterHQ/gitter.svg?style=flat-square)](https://gitter.im/opprTeam)
[![Twitter](https://flat.badgen.net/badge/icon/twitter?icon=twitter&label)](https://twitter.com/opprGroup)

Welcome to this *dataset* repository for our paper "[*Assertiveness-based Agent Communication for a Personalized Medicine on Medical Imaging Diagnosis*](https://doi.org/10.1145/3544548.3580682)" ([10.1145/3544548.3580682](https://doi.org/10.1145/3544548.3580682)) in [proceedings of the 2023 CHI Conference on Human Factors in Computing Systems](https://dl.acm.org/doi/proceedings/10.1145/3544548) ([CHI '23](https://chi2023.acm.org/)) presented during the "[AI in Health](https://programs.sigchi.org/chi/2023/program/session/97368)" track. In our work, several *datasets* are fostering innovation in higher-level functions for everyone, everywhere. By providing this repository, we hope to encourage the research community to focus on hard problems. In this repository, we present our *findings* of the AI models (*e.g.*, [`densenet-breast-classifier`](https://github.com/MIMBCD-UI/densenet-breast-classifier), [`ai-classifier-densenet161`](https://github.com/MIMBCD-UI/ai-classifier-densenet161), or [`ai-segmentation-densenet`](https://github.com/MIMBCD-UI/ai-segmentation-densenet) repositories), while classifying and segmenting several findings of patients for our [User Tests and Analysis 11 (UTA11)](https://github.com/MIMBCD-UI/meta/wiki/User-Research#test-11-assertiveness-based-assistant-pre-master-thesis-of-jo%C3%A3o-fernandes-) study. Here, we provide a *dataset* for the findings of the AI models for the patient diagnosis. Work and results are published on a top [Human-Computer Interaction (HCI)](https://en.wikipedia.org/wiki/Human%E2%80%93computer_interaction) conference named [CHI 2023](https://dl.acm.org/conference/chi) ([page](https://chi2023.acm.org/)). Results were analyzed and interpreted from our [`sa-uta11-results`](https://mimbcd-ui.github.io/sa-uta11-results) repository charts. On the same hand, the hereby *dataset* represents the pieces of information of both [BreastScreening](https://BreastScreening.github.io) and [MIDA](https://mida-project.github.io) projects. These projects are research projects that deal with the use of a recently proposed technique in literature: [Deep Convolutional Neural Networks (CNNs)](https://en.wikipedia.org/wiki/Convolutional_neural_network). From a developed User Interface (UI) and *framework*, these deep networks will incorporate [several datasets](https://github.com/MIMBCD-UI/meta/wiki/Datasets) in different modes. For more information about the available *datasets* please follow the [Datasets](https://github.com/MIMBCD-UI/meta/wiki/Datasets) page on the [Wiki](https://github.com/MIMBCD-UI/meta/wiki) of the [`meta`](https://github.com/MIMBCD-UI/meta) information repository. Last but not least, you can find further information on the [Wiki](https://github.com/MIMBCD-UI/dataset-uta11-findings/wiki) in this repository. We also have several demos to see in our [YouTube Channel](https://www.youtube.com/channel/UCPz4aTIVHekHXTxHTUOLmXw), please follow us.

## Citing

We kindly ask **scientific works and studies** that make use of the repository to cite it in their associated publications. Similarly, we ask **open-source** and **closed-source** works that make use of the repository to warn us about this use.

You can cite our work using the following BibTeX entry:

```
@inproceedings{10.1145/3544548.3580682,
author = {Calisto, Francisco Maria and Fernandes, Jo\~{a}o and Morais, Margarida and Santiago, Carlos and Abrantes, Jo\~{a}o Maria and Nunes, Nuno and Nascimento, Jacinto C.},
title = {Assertiveness-based Agent Communication for a Personalized Medicine on Medical Imaging Diagnosis},
year = {2023},
isbn = {9781450394215},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3544548.3580682},
doi = {10.1145/3544548.3580682},
abstract = {Intelligent agents are showing increasing promise for clinical decision-making in a variety of healthcare settings. While a substantial body of work has contributed to the best strategies to convey these agents’ decisions to clinicians, few have considered the impact of personalizing and customizing these communications on the clinicians’ performance and receptiveness. This raises the question of how intelligent agents should adapt their tone in accordance with their target audience. We designed two approaches to communicate the decisions of an intelligent agent for breast cancer diagnosis with different tones: a suggestive (non-assertive) tone and an imposing (assertive) one. We used an intelligent agent to inform about: (1) number of detected findings; (2) cancer severity on each breast and per medical imaging modality; (3) visual scale representing severity estimates; (4) the sensitivity and specificity of the agent; and (5) clinical arguments of the patient, such as pathological co-variables. Our results demonstrate that assertiveness plays an important role in how this communication is perceived and its benefits. We show that personalizing assertiveness according to the professional experience of each clinician can reduce medical errors and increase satisfaction, bringing a novel perspective to the design of adaptive communication between intelligent agents and clinicians.},
booktitle = {Proceedings of the 2023 CHI Conference on Human Factors in Computing Systems},
numpages = {20},
keywords = {Clinical Decision Support System, Healthcare, Breast Cancer},
location = {Hamburg, Germany},
series = {CHI '23}
}
```

## Table of contents

* [Prerequisites](#Prerequisites)
* [Usage](#Usage)
* [Roadmap](#Roadmap)
* [Contributing](#Contributing)
* [License & Copyright](#License--Copyright)
* [Team](#Team)
* [Acknowledgements](#Acknowledgements)

## Prerequisites

The following list is showing the required dependencies for this project to run locally:

* [Git](https://git-scm.com/) or any other Git or GitHub version control tool
* [Python](https://www.python.org/) (3.5 or newer)

Here are some tutorials and documentation, if needed, to feel more comfortable about using and playing around with this repository:

* [Python Tutorial](https://docs.python.org/3/tutorial/index.html)
* [Git Tutorial](https://git-scm.com/docs/gittutorial)
* [GitHub Quick Tutorial](https://guides.github.com/activities/hello-world/)

## Usage

Usage follow the instructions here to setup the current repository and extract the present data. To understand how the hereby repository is used for, read the following steps.

### Installation

At this point, the only way to install this repository is manual. Eventually, this will be accessible through [pip](https://pypi.org/project/pip/) or any other package manager, as mentioned on the [roadmap](#Roadmap).

Nonetheless, this kind of installation is as simple as cloning this repository. Virtually all Git and GitHub version control tools are capable of doing that. Through the console, we can use the command below, but other ways are also fine.

```bash
git clone https://github.com/MIMBCD-UI/dataset-uta11-findings.git
```

Optionally, the module/directory can be installed into the designated Python interpreter by moving it into the site-packages directory at the respective Python directory.

### Demonstration

Please, feel free to try out our demo. It is a script called `demo.py` at the `src/` directory. It can be used as follows:

```bash
python src/demo.py
```

Just keep in mind this is just a demo, so it does nothing more than reading the contents of the JSON file. Also, we did our best to make the demo as user-friendly as possible, so, above everything else, have fun! 😁

## Roadmap

[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/3819/badge)](https://bestpractices.coreinfrastructure.org/projects/3819)

We need to follow the repository goal, by addressing the thereby information. Therefore, it is of chief importance to scale this solution supported by the repository. The repository solution follows the best practices, achieving the [Core Infrastructure Initiative (CII)](https://bestpractices.coreinfrastructure.org/en/projects/3172) specifications.

Besides that, one of our goals involves creating a configuration file to automatically test and publish our code to pip or any other package manager. It will be most likely prepared for the [GitHub Actions](https://github.com/features/actions). Other goals may be written here in the future.

## Contributing

This project exists thanks to all the people who [contribute](CONTRIBUTING.md). We welcome everyone who wants to help us improve this downloader. As follows, we present some suggestions.

### Issuer

Either as something that seems missing or any need for support, just open a [new issue](https://github.com/MIMBCD-UI/dataset-uta11-findings/issues/new). Regardless of being a simple request or a fully-structured feature, we will do our best to understand them and, eventually, solve them.

### Developer

We like to develop, but we also like collaboration. You could ask us to add some features... Or you could want to do it yourself and fork this repository. Maybe even do some side-project of your own. If the latter ones, please let us share some insights about what we currently have.

## Information

The current information will summarize important items of this repository. In this section, we address all fundamental items that were crucial to the current information.

### Related Repositories

The following list, represents the set of related repositories for the presented one:

- [`sa-uta11-results`](https://github.com/MIMBCD-UI/sa-uta11-results)

- [`dataset-uta11-dicom`](https://github.com/MIMBCD-UI/dataset-uta11-dicom)

- [`dataset-uta11-rates`](https://github.com/MIMBCD-UI/dataset-uta11-rates)

- [`dataset-uta4-classifications`](https://github.com/MIMBCD-UI/dataset-uta4-classifications)

- [`dataset-uta7-annotations`](https://github.com/MIMBCD-UI/dataset-uta7-annotations)

- [`dataset-uta7-co-variables`](https://github.com/MIMBCD-UI/dataset-uta7-co-variables)

- [`dataset-uta10-annotations`](https://github.com/MIMBCD-UI/dataset-uta10-annotations)

### Dataset Resources

To publish our datasets we used a well known platform called [Kaggle](https://www.kaggle.com). For the purpose, three main resources [`uta4-singlemodality-vs-multimodality-nasatlx`](https://www.kaggle.com/MIMBCD-UI/uta4-singlemodality-vs-multimodality-nasatlx), [`uta4-sm-vs-mm-sheets`](https://www.kaggle.com/MIMBCD-UI/uta4-sm-vs-mm-sheets) and [`uta4-sm-vs-mm-sheets-nameless`](https://www.kaggle.com/MIMBCD-UI/uta4-sm-vs-mm-sheets-nameless) are published in this platform. Last but not least, *datasets* are also published at [figshare](https://figshare.com/projects/Single-Modality_vs_Multi-Modality/78372) and [OpenML](https://www.openml.org/d/42349) platforms.

### License & Copyright

Copyright &copy; 2023 [Instituto Superior Técnico](http://tecnico.ulisboa.pt/)

[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)

The [`dataset-uta11-findings`](https://github.com/MIMBCD-UI/dataset-uta11-findings) repository is distributed under the terms of [GNU AGPLv3](LICENSE) license and [CC-BY-SA-4.0](COPYING) copyright. Permissions of this license are conditioned on making available complete elements from this repository of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved.

### Team

Our team brings everything together sharing ideas and the same purpose, developing even better work. In this section, we will nominate the full list of important people for this repository, as well as respective links.

#### Authors

* Francisco Maria Calisto [ [Academic Website](https://web.tecnico.ulisboa.pt/francisco.calisto) | [ResearchGate](https://www.researchgate.net/profile/Francisco_Maria_Calisto) | [GitHub](https://github.com/FMCalisto) | [Twitter](https://twitter.com/FMCalisto) | [LinkedIn](https://www.linkedin.com/in/fmcalisto/) ]

* João Fernandes [ [ResearchGate](https://www.researchgate.net/profile/Joao-Fernandes-102) ]

* Margarida Morais [ [ResearchGate](https://www.researchgate.net/profile/Margarida_Morais2) ]

* Carlos Santiago [ [ResearchGate](https://www.researchgate.net/profile/Carlos-Santiago-4) ]

* João Maria Abrantes [ [ResearchGate](https://www.researchgate.net/profile/Joao-Abrantes-2) ]

* Nuno Nunes [ [ResearchGate](https://www.researchgate.net/profile/Nuno_Nunes2) ]

* Jacinto C. Nascimento [ [ResearchGate](https://www.researchgate.net/profile/Jacinto_Nascimento) ]

#### Promoters

* Hugo Lencastre
* Nádia Mourão
* Miguel Bastos
* Pedro Diogo
* João Bernardo
* Madalena Pedreira
* Mauro Machado

#### Companions

* Bruno Dias
* Bruno Oliveira
* Luís Ribeiro Gomes
* Pedro Miraldo

#### Acknowledgements

This work was partially supported by national funds through [FCT](http://fct.pt/) and [IST](http://tecnico.ulisboa.pt/) through the [UID/EEA/50009/2013](https://www.fct.pt/apoios/projectos/consulta/vglobal_projecto.phtml.en?idProjecto=147329&idElemConcurso=8999) project, [BL89/2017-IST-ID](http://ist-id.pt/en/) grant. We thank [Dr. Clara Aleluia](https://www.researchgate.net/profile/Clara_Aleluia) and her [radiology team](https://repositorio.hff.min-saude.pt/handle/10400.10/4?locale=en) of [HFF](https://hff.min-saude.pt/) for valuable insights and helping using the *assistants* on their daily basis. Further acknowledgments are provided inside the [`ACKNOWLEDGMENTS.md`](https://github.com/MIMBCD-UI/sa-uta11-results/blob/main/ACKNOWLEDGMENTS.md) file of the [`sa-uta11-results`](https://github.com/MIMBCD-UI/sa-uta11-results) repository. Additionally, we are grateful for the invaluable assistance provided by our colleagues of the [HCII](https://hcii.cmu.edu/) @ [CMU](https://cmu.edu/). We are indebted to those who gave their time and expertise to evaluate our work, who among others are giving us crucial information for the [BreastScreening](https://github.com/BreastScreening) project.

### Supporting

Our organization is a non-profit organization. However, we have many needs across our activity. From infrastructure to service needs, we need some time and contribution, as well as help, to support our team and projects.

<span>
  <a href="https://opencollective.com/oppr" target="_blank">
    <img src="https://opencollective.com/oppr/tiers/backer.svg" width="220">
  </a>
</span>

#### Contributors

This project exists thanks to all the people who contribute. [[Contribute](CONTRIBUTING.md)].

<span class="image">
  <a href="graphs/contributors">
    <img src="https://opencollective.com/oppr/contributors.svg?width=890" />
  </a>
</span>

#### Backers

Thank you to all our backers! 🙏 [[Become a backer](https://opencollective.com/oppr#backer)]

<span>
  <a href="https://opencollective.com/oppr#backers" target="_blank">
    <img src="https://opencollective.com/oppr/backers.svg?width=890">
  </a>
</span>

#### Sponsors

Support this project by becoming a sponsor. Your logo will show up here with a link to your website. [[Become a sponsor](https://opencollective.com/oppr#sponsor)]

<span>
  <a href="https://opencollective.com/oppr/sponsor/0/website" target="_blank">
    <img src="https://opencollective.com/oppr/sponsor/0/avatar.svg">
  </a>
</span>

<br />

<span>
  <a href="http://www.fct.pt/" title="FCT" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/fct_footer.png?raw=true" alt="fct" width="20%" />
  </a>
</span>
<span>
  <a href="https://www.fccn.pt/en/" title="FCCN" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/fccn_footer.png?raw=true" alt="fccn" width="20%" />
  </a>
</span>
<span>
  <a href="https://www.ulisboa.pt/en/" title="ULisboa" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/ulisboa_footer.png?raw=true" alt="ulisboa" width="20%" />
  </a>
</span>
<span>
  <a href="http://tecnico.ulisboa.pt/" title="IST" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/ist_footer.png?raw=true" alt="ist" width="20%" />
  </a>
</span>
<span>
  <a href="http://hff.min-saude.pt/" title="HFF" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/hff_footer.png?raw=true" alt="hff" width="20%" />
  </a>
</span>
<span>
  <a href="https://www.chtmad.min-saude.pt/" title="CHTMAD" target="_blank">
    <img src="https://raw.githubusercontent.com/MIMBCD-UI/meta/master/brands/chtmad_footer.png" alt="chtmad" width="10%" />
  </a>
</span>

##### Departments

<span>
  <a href="http://dei.tecnico.ulisboa.pt" title="DEI" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/dei_footer.png?raw=true" alt="dei" width="20%" />
  </a>
</span>
<span>
  <a href="http://deec.tecnico.ulisboa.pt" title="DEEC" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/deec_footer.png?raw=true" alt="dei" width="20%" />
  </a>
</span>

##### Laboratories

<span>
  <a href="http://sipg.isr.tecnico.ulisboa.pt/" title="SIPG" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/sipg_footer.png?raw=true" alt="sipg" width="20%" />
  </a>
</span>
<span>
  <a href="http://welcome.isr.tecnico.ulisboa.pt/" title="ISR" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/isr-lisboa_footer.png?raw=true" alt="isr" width="20%" />
  </a>
</span>
<span>
  <a href="http://larsys.pt/" title="LARSys" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/larsys_footer.png?raw=true" alt="larsys" width="20%" />
  </a>
</span>
<span>
  <a href="https://iti.larsys.pt/" title="ITI" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/iti_footer.png?raw=true" alt="iti" width="20%" />
  </a>
</span>
<span>
  <a href="http://www.inesc-id.pt/" title="INESC-ID" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/inesc-id_footer.png?raw=true" alt="inesc-id" width="20%" />
  </a>
</span>

##### Domain

<span>
  <a href="https://europa.eu/" title="EU" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/eu_footer.png?raw=true" alt="eu" width="20%" />
  </a>
</span>
<span>
  <a href="https://www.portugal.gov.pt/" title="Portugal" target="_blank">
    <img src="https://github.com/mida-project/meta/blob/master/brands/pt_footer.png?raw=true" alt="pt" width="20%" />
  </a>
</span>
