Course Overview, https://github.com/Kwangkee/Gachon/blob/main/Lecture_2022_Fall-1.pdf  
Instructor: 이광기 (Kwangkee Lee, kwangkeelee@gmail.com)
- [1주차에] 본 class 에 기대하는 바, 제안사항 알려주시고, [이후] 질문/제안 언제든 주시기 바랍니다.
- 숙제, 발표자료는 하루 전 까지 [[사이버캠퍼스](https://cyber.gachon.ac.kr/course/view.php?id=79839)]에 upload 해 주세요.

#### Slides
- Week-1 Slide: https://github.com/Kwangkee/Gachon/blob/main/slides/FL_Introduction_2022_Fall.pdf  
- Week-2 Slide: https://github.com/Kwangkee/Gachon/blob/main/slides/FL_Platforms_2022_Fall.pdf  
- Week-4 Slide: https://github.com/Kwangkee/Gachon/blob/main/slides/FL_ClientContribution_2022_Fall.pdf
- Week-7 Slide: https://github.com/Kwangkee/Gachon/blob/main/slides/FL_Medical_2022_Fall.pdf

#### Awesome Federated Machine Learning
- https://www.google.com/search?q=awesome+Federated+Learning
- https://github.com/innovation-cat/Awesome-Federated-Machine-Learning
- https://github.com/ChanChiChoi/awesome-Federated-Learning
- https://github.com/chaoyanghe/Awesome-Federated-Learning


***
## Week-1
#### 강의 (Instructor)  
- [**Must-read**] Federated Learning Tutorial@NeurIPS 2020, https://sites.google.com/view/fl-tutorial/, [slides] https://drive.google.com/file/d/1QGY2Zytp9XRSu95fX2lCld8DwfEdcHCG/view
  >Part I: What is Federated Learning?  
  >Part II: Federated Optimization  
  >*Part III: Privacy for Federated Learning and Analytics*  
  >Part IV: Open Problems and Other Topics  

- FL Intro, https://github.com/Kwangkee/FL/blob/main/FL@Intro.md#fl-introduction  
  >Communication-Efficient Learning of Deep Networks from Decentralized Data, https://arxiv.org/abs/1602.05629  
  >Towards Federated Learning at Scale: System Design, https://arxiv.org/abs/1902.01046  
  >[Recommend] Advances and Open Problems in Federated Learning, https://arxiv.org/abs/1912.04977   

- Virginia Smith, https://www.cs.cmu.edu/~smithv/, 
  - ML with Large Datasets, Fall 2021, https://10605.github.io/fall2021/  
    >Introduction ([slides](https://drive.google.com/file/d/1-0aBTILgeMKn6FDfOBfg-hG1qCtRNNNr/view?usp=sharing), video)  
    >Federated Learning ([slides](https://drive.google.com/file/d/13WrVAophCH6pgkgRJoFhhf2Fndlr-zin/view?usp=sharing), video)  
  - ML with Large Datasets, Fall 2022, https://10605.github.io/ 

#### Week-1 실습 (TA: 김대열 박사)
- [발표] DNN 리류, https://github.com/Kwangkee/Gachon/blob/main/slides/TA_DL_overview.pdf
- [실습] PyTorch/Tensorflow 리뷰/설치, Tutorial/Sample code 

***
## Week-2
#### 강의 (Instructor)  
- [**Must-read**] FLRA: a reference architecture of federated learning systems, https://github.com/Kwangkee/FL/blob/main/FL%40CSIRO.md#flra-a-reference-architecture-for-federated-learning-systems

- 연합학습 Open Source Platform https://github.com/Kwangkee/FL/blob/main/FL@Platform.md
  >[**Must-read**] Flower: A Friendly Federated Learning Research Framework, https://arxiv.org/abs/2007.14390  

- FedScale: Benchmarking Model and System Performance of Federated Learning at Scale, https://github.com/Kwangkee/FL/blob/main/FL%40FedScale.md  
  >[**Must-read**] FedScale: Benchmarking Model and System Performance of Federated Learning at Scale, https://arxiv.org/abs/2105.11367   
  >[Recommend] Swan, https://github.com/Kwangkee/FL/blob/main/FL%40FedScale.md#swan   
  >[slides] http://www-personal.umich.edu/~fanlai/assets/docs/fedscale-icml-slides.pdf from http://www-personal.umich.edu/~fanlai/  
  >Open-Source Systems for Federated Learning | [Stanford MLSys](https://mlsys.stanford.edu/) #48, https://www.youtube.com/watch?v=TcbOMbg4F9g

#### Week-2 실습 (TA: 김진수)
- [발표] 연합학습 Open Source Platform 리뷰, https://github.com/Kwangkee/Gachon/blob/main/slides/TA_FL%20Open-Source%20Platform.pdf
- [발표] 연합학습 Open Source Platform 리뷰-2, https://github.com/Kwangkee/Gachon/blob/main/slides/TA_FL%20Open-Source%20Platform-2.pdf
- [실습] Flower/FedScale 설치, Tutorial/Sample code

***
## Week-3
#### 강의 (Instructor)  
- 연합학습 이슈 : Data/System Heterogeneity in Federated Learning, Personalized FL
  >Stanford MLSys Seminar Episode 3: Virginia Smith, On Heterogeneity in Federated Settings, https://www.youtube.com/watch?v=laCyJICLyWg

- 동적인 디바이스 환경에서 적응적 연합학습, https://github.com/Kwangkee/FL/blob/main/AFL.md  

- Personalized federated learning, https://github.com/Kwangkee/FL/blob/main/FL@Nanyang.md#towards-personalized-federated-learning
  >[**Must-read**] Towards Personalized Federated Learning, https://arxiv.org/abs/2103.00710  
#### Week-3 실습 (TA: 김진수)
- Federated MetaSense, 적응적 연합학습
#### Week-3 학생 발표
- [양세모] [**Must-read**] 연합학습시스템에서의 MLOps 구현 방안 연구, 
  - http://www.jics.or.kr/digital-library/25791
  - https://github.com/Kwangkee/Gachon/blob/main/slides/%EC%97%B0%ED%95%A9%ED%95%99%EC%8A%B5%20%EC%8B%9C%EC%8A%A4%ED%85%9C%EC%97%90%EC%84%9C%EC%9D%98%20MLOps%20%EA%B5%AC%ED%98%84%20%EB%B0%A9%EC%95%88%20%EC%97%B0%EA%B5%AC.pdf
- [이기훈] Open Source Platform 사용기, 실습 결과, https://github.com/Liky98/Federated_Learning/blob/master/README/Week3%203f7a8157a4b6403ab14d2ee8e5bcf967.md
- [시경요] Open Source Platform 사용기, 실습 결과, https://github.com/qq490800573/FL-Platform-Homework/tree/main/Week3-Homework

## Week-4
#### 강의 (Instructor)  
- Client Selection, https://github.com/Kwangkee/FL/blob/main/FL%40ClientSelection.md
- [**Must-read**] Oort: Efficient Federated Learning via Guided Participant Selection, https://github.com/Kwangkee/FL/blob/main/FL%40ClientSelection.md#oort  
  >- https://www.usenix.org/conference/osdi21/presentation/lai  
  >- Presentation Video: https://www.youtube.com/watch?v=5npOel4T4Mw  
  >- slides: https://www.usenix.org/system/files/osdi21_slides_lai.pdf  
- FedBalancer, https://github.com/Kwangkee/FL/blob/main/AFL.md#t1-kaist
  >- https://nmsl.kaist.ac.kr/projects/fedbalancer/, 이기종 사용자 기기가 포함된 환경에서의 최적화된 사용자 학습 데이터 선택 및 연합학습 라운드의 데드라인 제어를 통한 효율적인 연합학습 알고리즘 연구
  >- Slides: https://drive.google.com/file/d/1zlN6er5xOcQgiLQCHaGVGso9r5Mvm_Ms/view
  >- Conference Presentation: https://www.youtube.com/watch?v=q3NeIUjSjqg&t=2s

- Etc
  >- Ditto: Fair and Robust Federated Learning Through Personalization, https://proceedings.mlr.press/v139/li21h.html   
  >- YaeJeeCho@CM https://github.com/Kwangkee/FL/blob/main/FL@CarnegieMellon.md#yae-jee-cho  

- FL with Noisy Labels  
  >- Federated Learning with Noisy Labels, https://arxiv.org/abs/2208.09378  
  >- Overcoming Noisy and Irrelevant Data in Federated Learning, https://arxiv.org/abs/2001.08300    
  >- Robust Federated Learning with Noisy Labels, KAIST, https://ieeexplore.ieee.org/document/9713942

- 연합학습 Public Data, PFL Benchmarking, https://github.com/Kwangkee/FL/blob/main/FL@Benchmark.md

#### Invited Talk (신재민/KAIST)
- Efficient Federated Learning Approaches on Heterogeneous Clients, 이기종 클라이언트 위 효율적 연합학습 방법론, https://github.com/Kwangkee/Gachon/blob/main/slides/TA_FedBalancer_%EC%8B%A0%EC%9E%AC%EB%AF%BC_20221007.pdf
- FedBalancer, https://github.com/Kwangkee/FL/blob/main/FL@ClientSelection.md#fedbalancer

## Week-5
#### 강의 (Instructor)  
- 연합학습의 Digital Healthcare 분야 적용 사례
- 디지털 헬스케어를 위한 블록체인 융합 원격임상시험 서비스 개발, https://drive.google.com/drive/u/0/folders/1qV5jN-KspZWYuUZEzx0mzLEYPsomzhko
- Equideum Health, https://github.com/Kwangkee/FL/blob/main/BCFL%40Equideum.md
- rPPG, https://github.com/Kwangkee/rPPG, 원격임상시험 D-2 리뷰

#### Week-5 실습 (TA: 김대열 박사)
- [발표] rPPG 리뷰 및 실습, https://github.com/Kwangkee/Gachon/blob/main/slides/TA_rPPG_Overview.pdf
- [논문] 딥러닝 기반 rPPG 모델 사용을 위한 경량 모델 연구, https://github.com/Kwangkee/Gachon/blob/5dd38ea670a14d0f0dd71fd789ce879c2be9d9a4/slides/%EC%9D%98%EB%A3%8C%EC%A0%95%EB%B3%B4%ED%95%99%ED%9A%8C_2022%EC%B6%94%EA%B3%84_%EB%94%A5%EB%9F%AC%EB%8B%9D%20%EA%B8%B0%EB%B0%98%20rPPG%20%EB%AA%A8%EB%8D%B8%20%EC%82%AC%EC%9A%A9%EC%9D%84%20%EC%9C%84%ED%95%9C%20%EA%B2%BD%EB%9F%89%20%EB%AA%A8%EB%8D%B8%20%EC%97%B0%EA%B5%AC.pdf
- [논문] Assessment of ROI Selection for Facial Video-Based rPPG(MDPI Sensors 2021):  [T3-1] 헬스케어 서비스 분야에서, 원격-PPG 기반 생체징후인식 실세계 적용 시나리오에 적응적 연합학습 기술을 적용하기 위한 기반기술, https://www.mdpi.com/1424-8220/21/23/7923  
- [논문] 안면 이미지 데이터를 이용한 실시간 생체 징후 측정 시스템, https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002699582 


## Week-6
#### 강의 (Instructor)  
- 연합학습의 medical 분야 적용, https://github.com/Kwangkee/FL/blob/main/FL@Medical.md
  >[**Must-read**] [[Contribution-Aware Federated Learning for Smart Healthcare](https://github.com/Kwangkee/FL/blob/main/FL@Nanyang.md#carefl)], https://ojs.aaai.org/index.php/AAAI/article/view/21505   
  >[Recommend] [[삼성병원: 신수용 교수](https://github.com/Kwangkee/FL/blob/main/FL@Medical.md#%EC%82%BC%EC%84%B1%EB%B3%91%EC%9B%90-%EC%8B%A0%EC%88%98%EC%9A%A9-%EA%B5%90%EC%88%98)]   
  >Artificial Intelligence in Healthcare, https://biods220.stanford.edu/, Distributed Learning, Security, and Privacy lecture14.pdf, https://biods220.stanford.edu/lectures/lecture14.pdf

***
## Week-7
#### 강의 (Instructor)  
- 블록체인 융합 연합학습, https://github.com/Kwangkee/FL/blob/main/BCFL%40Korea.md
  >[**Must-read**] 2CP: Decentralized Protocols to Transparently Evaluate Contributivity in Blockchain Federated Learning Environments, https://arxiv.org/abs/2011.07516, Code: https://github.com/cai-harry/2CP  
  >[Recommend] 연합학습의 인센티브 플랫폼으로써 이더리움 스마트 컨트랙트를 시행하는 경우의 실무적 고려사항, https://github.com/Kwangkee/FL/blob/main/BCFL%40Korea.md#%EB%B6%80%EA%B2%BD%EB%8C%80

- [Recommend][한글 유튜브] Web3 기술 인프라 , https://youtu.be/2cpUO1XN528?t=3173
- [Udemy Course] https://www.udemy.com/course/master-ethereum-and-solidity-programming-with-real-world-apps/?utm_source=email-sendgrid&utm_medium=1771964&utm_campaign=2022-10-20&utm_term=50683248&utm_content=promo

#### 실습 (TA: 고은수/이노피아)
- [발표, 실습] BCFL, https://github.com/Kwangkee/Gachon/blob/main/slides/TA_BCFL_%EA%B3%A0%EC%9D%80%EC%88%98.pdf
- 블록체인 기반 연합학습을 위한 퍼런스 아키텍처, https://github.com/Kwangkee/Gachon/blob/main/samples/%EB%B8%94%EB%A1%9D%EC%B2%B4%EC%9D%B8%EC%97%B0%ED%95%A9%ED%95%99%EC%8A%B5_%EC%9D%98%EB%A3%8C%EC%9D%B8%EA%B3%B5%EC%A7%80%EB%8A%A5%ED%95%99%ED%9A%8C_2022%EC%B6%94%EA%B3%84_20221013.pdf

***
## Week-8
#### 강의 (Instructor)  
- 블록체인 융합 연합학습, https://github.com/Kwangkee/FL/blob/main/BCFL%40Korea.md
  >[**Must-read**] [[Towards Trustworthy AI: Blockchain-based Architecture Design for Accountability and Fairness of Federated Learning Systems](https://github.com/Kwangkee/FL/blob/main/FL%40CSIRO.md#towards-trustworthy-ai)], https://scholar.google.com/citations?view_op=view_citation&hl=ko&user=TuL21poAAAAJ&sortby=pubdate&citation_for_view=TuL21poAAAAJ:koF6b02d8EEC
  >[Recommend] https://github.com/Kwangkee/FL/blob/main/BCFL%40Korea.md#%EC%84%9C%EC%9A%B8%EB%8C%80


***
## Week-9
#### 강의 (Instructor)  

#### Invited Talk (성균관대 신성국/김광수 교수님)

***
## Week-10
#### 강의 (Instructor)  

#### Invited Talk (성균관대 우홍욱 교수님)
- 


****

TA
|주차|TA 발표|실습|담당 TA|
|---|---|--|--|
|1|DNN 리뷰, PyTorch/TF 리뷰, DNN 환경|Git 계정, PyTorch 설치, Tutorial/Sample code|김대열|
|2|연합학습 Open Source Platform (Flower/FedScale) 리뷰|설치, Tutorial/Sample code|김진수|
|3|Federated MetaSense, 적응적 연합학습|적응적 연합학습|김진수|
|4|연합학습 Public Data, Benchmarking 리뷰|PFL Benchmarking 설치, Tutorial/Sample code|김진수|
|5|rPPG 리뷰|rPPG code 리뷰|김대열|
|6|원격임상시험 D-3 리뷰|PoC 결과|양세모|
|7|BC 리뷰|Ethereum Simulator, Solidity|고은수|
|8|BCFL 리뷰|2CP Simulator|고은수|


****

[etc]
- [Invited Talk] KAIST MetaSense, FedBalancer
- Stanford MLSys Seminar Series, https://mlsys.stanford.edu/
- MLOps
  >MLOps System Design for Development and Production | [Stanford MLSys](https://mlsys.stanford.edu/) #44, https://www.youtube.com/watch?v=TcbOMbg4F9g  
- Virginia Smith, https://www.cs.cmu.edu/~smithv/, ML with Large Datasets, Fall 2021, https://10605.github.io/fall2021/
  >Aug 31	Introduction ([slides](https://drive.google.com/file/d/1-0aBTILgeMKn6FDfOBfg-hG1qCtRNNNr/view?usp=sharing), video)   
  >Nov 23	Federated Learning ([slides](https://drive.google.com/file/d/13WrVAophCH6pgkgRJoFhhf2Fndlr-zin/view?usp=sharing), [video](https://scs.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=e987cd72-7681-403a-942b-ade9014cd267))   
- CS 330: Deep Multi-Task and Meta Learning, http://cs330.stanford.edu/
- BIODS220 (CS271, BIOMEDIN220) Artificial Intelligence in Healthcare, https://biods220.stanford.edu/
  >Lecture 14	Nov 15 (Mon)	Distributed Learning, Security, and Privacy	lecture14.pdf, https://biods220.stanford.edu/lectures/lecture14.pdf  

