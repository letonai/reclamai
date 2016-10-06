# Reclamai

Baseado em: [http://pastebin.com/WMEh802V](http://pastebin.com/WMEh802V)

Python para verificar a velocidade da conexão com a Internet e "reclamar" no twitter caso a conexão 
não esteja dentro de uma velocidade mínima aceitavel.

Dependencias:

Máquina com linux e python Do'h! (raspberry?).

Biblioteca Python do twitter:

```sh
pip install twitter
```

Cliente de teste de volocidade me modo texto do SpeedTest:

```sh
apt install speedtest-cli 
```

Para utilizar basta editar o arquivo config.py e adicionar as informações necessárias.

Para executar: 

```sh
./reclamai.py
```

Recomendo colocar na crontab a cada 1h:


```sh
0 * * * * /path/reclamai.py
```
