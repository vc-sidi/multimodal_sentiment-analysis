# multimodal_sentiment-analysis
- Link pra Resumo dos artigos: https://docs.google.com/spreadsheets/d/10K6Y3o2ECW058C-2lwY7mLbrVwjGL7HZSuw71I1Uu0Y/edit?usp=sharing
- Dataset:
  - http://www.t4sa.it/:
      - b-t4sa_imgs.tar (63GB): contains only the 470,586 images of the B-T4SA dataset and train/val/test splits used in our experiments;
      - t4sa_text_sentiment.tsv (74MB): contains the textual sentiment classification of the 1,179,957 selected tweets of the T4SA dataset;
      - raw_tweets_text.csv (414MB): contains id and text of all the collected ~3.4 M tweets
     
- TO DO:
  - Definir problema:
      1. Utilizar o Deep Fusion em conjunto com classificador individual de texto e imagem para depois fazer um ensemble
  - [x] Escrita da especificação até dia até dia 30/12/2021.
  - [ ] Filtragem da base de imanges:
    - [ ] Determinar tamannho da imagens;
    - [ ] Criar novo dataset balancedo.
  - [ ] Reutilizar implementação do VADER;
