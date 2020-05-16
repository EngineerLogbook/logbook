# Generate database model graph

Change to the engbook directory
```bash
cd engbook
```


Make sure that you've installed all packages from requirements.txt. 

```bash
python -m pip install -r requirements.txt
```


Propagate all changes in models.py to your database.


```
python manage.py makemigrations
```
```    
python manage.py migrate
```

Generate the model graphs : 

__PNG__
```    
python manage.py graph_models -o dbModelGraphs/models.png
```

__SVG__
```
python manage.py graph_models -o dbModelGraphs/models.svg
```



___
## Troubleshooting

In case the command `pip install pygraphviz` fails with an error like

``` 
Package 'libcgraph', required by 'virtual:world', not found
```

Then you need to install the `graphviz` package for your respective operationg system first. 

__Windows__

```
```

__MacOS__


```
brew install graphviz
```

__Ubuntu 18.04 LTS__

```
sudo apt update -y && sudo apt install -y graphviz
```

__Arch__

Install the `graphviz` package from the AUR






___
## Reference Documentation

[Django-Extensions](https://django-extensions.readthedocs.io/en/latest/graph_models.html#default-settings)
