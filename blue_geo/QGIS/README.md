# 🌐 QGIS

🌐 an AI terraform for [QGIS](https://www.qgis.org/).

```bash
pip install blue-geo
```

```bash
QGIS help
```
```bash
@download \
	[.|<object-name>] \
	[open,~QGIS]
 . download object and its QGIS dependencies.
QGIS \
	expressions \
	push \
	[push]
 . push QGIS expressions.
   from: $abcli_QGIS_path_expressions
   to: $abcli_QGIS_path_expressions_git
QGIS \
	expressions \
	pull
 . pull QGIS expressions.
   from: $abcli_QGIS_path_expressions_git
   to: $abcli_QGIS_path_expressions
QGIS \
	seed \
	[screen]
 . seed 🌱 QGIS.
QGIS \
	serve[r] \
	[start]
 . start QGIS server.
```

to terraform QGIS, generate the seed 🌱,

```bash
QGIS seed
```

and paste it in the Python Console in QGIS.

![image](https://github.com/kamangir/assets/blob/main/blue-geo/QGIS-python-console.png?raw=true)

![image](https://raw.githubusercontent.com/kamangir/assets/main/blue-geo/QGIS.png)
