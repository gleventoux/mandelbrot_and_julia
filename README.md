# mandelbrot_and_julia

Ce package python fournit des utilitaires pour tracer les ensembles de Mandelbrot et de Julia et vérifier expérimentalement l'appartenance de points à ces ensembles.

## Installation

Cloner le repo et l'installer avec pip.

```
git clone https://github.com/gleventoux/mandelbrot_and_julia.git
cd mandelbrot_and_julia
pip install .
```

## Dépendances

Le projet dépend des bliothèques suivantes qui sont automatiquement installées lors de l'installation du package.
- [Numpy](https://numpy.org/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)
- [Pytest](https://docs.pytest.org/en/7.2.x/)

## Tutoriel
Pour utiliser l'utilitaire dans un script python, commencer par importer le module `utils.py`.

```
from mandelbrot_and_julia import utils
```

Les quatre méthodes disponibles sont:

- `is_in_mandelbrot`: Vérifie l'appartenence d'un point à l'ensemble de Mandelbrot. La condition d'appartenance étant que la suite générée par ce point est bornnée,
on ne calcul qu'un nombre limité de termes (paramètre optionnel **max_iter**) et on regarde si ils sont tous à l'intérieur du disque centré sur l'origine de rayon **threshold** (paramètre optionnel)

- `is_in_julia` : Vérifie l'appartenance d'un point à l'ensenble de julia. Le procédé est quasiment identique au cas précédent. En revanche, l'argument **c** est ajouté pour définir l'ensenble
de Julia en question et le rayon du disque de contrôle est fixé à 2.

- `plot_mandelbrot`: Trace l'ensemble de Mandelbrot puis sauvegarde l'image dans le dossier `output` sous le nom donné par l'utilisateur comprenant l'extension via l'argument optionnel **figname**.
L'utilisateur peut aussi choisir la fenêtre de visualisation via les arguments optionnels **zmin** et **zmax** qui sont respectivement les coins bas-gauche et haut-droit de cette dernière.

- `plot_julia`: Trace l'ensemble de Julia pour un complexe **c** donné selon le même procédé.


## CLI

Deux cli ont été implementées pour permettre le tracer des fractales directement depuis le terminal.

```
MandelbrotPlot [--zmin zmin] [--zmax zmax] [--pixel_size pixel_size] [--max_iter max_iter] [-o figname]
```
```
JuliaPlot [-c candidate] [--zmin zmin] [--zmax zmax] [--pixel_size pixel_size] [--max_iter max_iter] [-o figname]
```

## Documentation

Pour plus d'informations sur les méthodes présentées, consulter la documentation générée automatiquement par [sphinx](https://www.sphinx-doc.org/en/master/).
Pour cela, ouvrir le fichier `doc/build/html/index.html` avec votre naviguateur.

## Résultats

Vous trouverez dans cette section quelques images obtenues avec notre programme.

<div align=center>
  
<figure>
  <img src="img/Mandelbrot.png" alt="drawing" width="500"/>
</figure>
<p>Fig.1 - Ensemble de Mandelbrot</p>
  
</div>
  





