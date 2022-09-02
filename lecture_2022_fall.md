Course Overview, https://github.com/Kwangkee/Gachon/blob/main/Lecture_2022_Fall-1.pdf  
Instructor: 이광기 (Kwangkee Lee, kwangkeelee@gmail.com)
- [1주차에] 본 class 에 기대하는 바, 제안사항 알려주시고, [이후] 질문/제안 언제든 주시기 바랍니다.
- 숙제, 발표자료는 하루 전 까지 [[사이버캠퍼스](https://cyber.gachon.ac.kr/course/view.php?id=79839)]에 upload 해 주세요.

***
## 1주
#### 강의 (Instructor)  
- [Must-read] Federated Learning Tutorial@NeurIPS 2020, https://sites.google.com/view/fl-tutorial/, [slides] https://drive.google.com/file/d/1QGY2Zytp9XRSu95fX2lCld8DwfEdcHCG/view
  >Part I: What is Federated Learning?  
  >Part II: Federated Optimization  
  >*Part III: Privacy for Federated Learning and Analytics*  
  >Part IV: Open Problems and Other Topics  

- FL Intro, https://github.com/Kwangkee/FL/blob/main/FL@Intro.md#fl-introduction  
  >Communication-Efficient Learning of Deep Networks from Decentralized Data, https://arxiv.org/abs/1602.05629  
  >Towards Federated Learning at Scale: System Design, https://arxiv.org/abs/1902.01046  
  >[Recommend] Advances and Open Problems in Federated Learning, https://arxiv.org/abs/1912.04977   

- Virginia Smith, https://www.cs.cmu.edu/~smithv/, ML with Large Datasets, Fall 2021, https://10605.github.io/fall2021/  
  >Introduction ([slides](https://drive.google.com/file/d/1-0aBTILgeMKn6FDfOBfg-hG1qCtRNNNr/view?usp=sharing), video)  
  >Federated Learning ([slides](https://drive.google.com/file/d/13WrVAophCH6pgkgRJoFhhf2Fndlr-zin/view?usp=sharing), video)  
#### 실습 (TA)
- [발표] DNN 리뷰, https://github.com/Kwangkee/Gachon/blob/e959d9d076657d6625398dd363dd6dd49663de5d/slides/220901_DL_overview.pdf
- [실습] PyTorch/Tensorflow 리뷰/설치, Tutorial/Sample code 

***
## 2주
#### 강의 (Instructor)  
- [Must-read] FLRA: a reference architecture of federated learning systems, https://github.com/Kwangkee/FL/blob/main/FL%40CSIRO.md#flra-a-reference-architecture-for-federated-learning-systems

- 연합학습 Open Source Platform https://github.com/Kwangkee/FL/blob/main/FL@Platform.md
  >[Must-read] Flower: A Friendly Federated Learning Research Framework, https://arxiv.org/abs/2007.14390  

- FedScale: Benchmarking Model and System Performance of Federated Learning at Scale, https://github.com/Kwangkee/FL/blob/main/FL%40FedScale.md  
  >[Must-read] FedScale: Benchmarking Model and System Performance of Federated Learning at Scale, https://arxiv.org/abs/2105.11367   
  >[Recommend] Swan, https://github.com/Kwangkee/FL/blob/main/FL%40FedScale.md#swan   
  >[slides] http://www-personal.umich.edu/~fanlai/assets/docs/fedscale-icml-slides.pdf from http://www-personal.umich.edu/~fanlai/  
  >Open-Source Systems for Federated Learning | [Stanford MLSys](https://mlsys.stanford.edu/) #48, https://www.youtube.com/watch?v=TcbOMbg4F9g

#### 실습 (TA)
- [발표] 연합학습 Open Source Platform (Flower/FedScale) 리뷰
- [실습] Flower 설치, Tutorial/Sample code
#### 학생 발표
- [학생#1 발표] https://github.com/Kwangkee/FL/blob/main/FL@Intro.md
- [학생#2 발표] https://github.com/Kwangkee/FL/blob/main/FL@Intro.md

***
## 3주
#### 강의 (Instructor)  
- 연합학습 이슈 : Data/System Heterogeneity in Federated Learning, Personalized FL
  >Stanford MLSys Seminar Episode 3: Virginia Smith, On Heterogeneity in Federated Settings, https://www.youtube.com/watch?v=laCyJICLyWg

- 동적인 디바이스 환경에서 적응적 연합학습, https://github.com/Kwangkee/FL/blob/main/AFL.md  

- Personalized federated learning, https://github.com/Kwangkee/FL/blob/main/FL@Nanyang.md#towards-personalized-federated-learning
  >[Must-read] Towards Personalized Federated Learning, https://arxiv.org/abs/2103.00710  
#### 실습 (TA)
- Federated MetaSense, 적응적 연합학습
#### 학생 발표
- [학생#1 발표] Open Source Platform 사용기, 실습 결과, https://github.com/Kwangkee/FL/blob/main/FL@Platform.md, Flower
- [학생#2 발표] Open Source Platform 사용기, 실습 결과, https://github.com/Kwangkee/FL/blob/main/FL@Platform.md, FedScale  

## 4주
#### 강의 (Instructor)  
- Client Selection, https://github.com/Kwangkee/FL/blob/main/FL%40ClientSelection.md
  >Ditto: Fair and Robust Federated Learning Through Personalization, https://proceedings.mlr.press/v139/li21h.html   
  >[Must-read] Oort: Efficient Federated Learning via Guided Participant Selection, https://github.com/Kwangkee/FL/blob/main/FL%40ClientSelection.md#oort  
  >YaeJeeCho@CM https://github.com/Kwangkee/FL/blob/main/FL@CarnegieMellon.md#yae-jee-cho  

- FL with Noisy Labels  
  >Federated Learning with Noisy Labels, https://arxiv.org/abs/2208.09378
  >Overcoming Noisy and Irrelevant Data in Federated Learning, https://arxiv.org/abs/2001.08300    
  >Robust Federated Learning with Noisy Labels, KAIST, https://ieeexplore.ieee.org/document/9713942

- 연합학습 Public Data, PFL Benchmarking, https://github.com/Kwangkee/FL/blob/main/FL@Benchmark.md

#### 실습 (TA)
- [발표] 연합학습 Public Data, PFL Benchmarking 개요
- [실습] 연합학습 Public Data, PFL Benchmarking 설치, Tutorial/Sample code 

#### 학생 발표
- [학생#1 발표] Open Source Platform 사용기, 실습 결과, https://github.com/Kwangkee/FL/blob/main/FL@Platform.md, FedML, FLSim, ...   
- [학생#2 발표] Open Source Platform 사용기, 실습 결과, https://github.com/Kwangkee/FL/blob/main/FL%40FedScale.md#swan, Swan  

## 5주
#### 강의 (Instructor)  
- 연합학습의 Digital Healthcare 분야 적용 사례
- 디지털 헬스케어를 위한 블록체인 융합 원격임상시험 서비스 개발, https://drive.google.com/drive/u/0/folders/1qV5jN-KspZWYuUZEzx0mzLEYPsomzhko
- Equideum Health, https://github.com/Kwangkee/FL/blob/main/BCFL%40Equideum.md
- rPPG, https://github.com/Kwangkee/rPPG, 원격임상시험 D-2 리뷰

#### 실습 (TA)
- [발표] rPPG 리뷰
- [실습] rPPG 실습

#### 학생 발표
- [학생#1 발표] PFL Benchmark 사용기, 실습 결과, https://github.com/Kwangkee/FL/blob/main/FL@Benchmark.md
- [학생#2 발표] PFL Benchmark 사용기, 실습 결과, https://github.com/Kwangkee/FL/blob/main/FL@Benchmark.md

## 6주
#### 강의 (Instructor)  
- 연합학습의 medical 분야 적용, https://github.com/Kwangkee/FL/blob/main/FL@Medical.md
  >[Must-read] [[Contribution-Aware Federated Learning for Smart Healthcare](https://github.com/Kwangkee/FL/blob/main/FL@Nanyang.md#carefl)], https://ojs.aaai.org/index.php/AAAI/article/view/21505   
  >[Recommend] [[삼성병원: 신수용 교수](https://github.com/Kwangkee/FL/blob/main/FL@Medical.md#%EC%82%BC%EC%84%B1%EB%B3%91%EC%9B%90-%EC%8B%A0%EC%88%98%EC%9A%A9-%EA%B5%90%EC%88%98)]   
  >Artificial Intelligence in Healthcare, https://biods220.stanford.edu/, Distributed Learning, Security, and Privacy lecture14.pdf, https://biods220.stanford.edu/lectures/lecture14.pdf

#### 실습 (TA)
- [발표] 원격임상시험 D-3 리뷰
- [실습] 원격임상시험 D-3 PoC 결과

#### 학생 발표
- [학생#1 발표] Benchmark 사용기, 실습 결과, https://github.com/Kwangkee/FL/blob/main/FL@Benchmark.md

## 7주
#### 강의 (Instructor)  
- 블록체인 융합 연합학습, https://github.com/Kwangkee/FL/blob/main/BCFL%40Korea.md
  >[Must-read] 2CP: Decentralized Protocols to Transparently Evaluate Contributivity in Blockchain Federated Learning Environments, https://arxiv.org/abs/2011.07516, Code: https://github.com/cai-harry/2CP  
  >[Recommend] 연합학습의 인센티브 플랫폼으로써 이더리움 스마트 컨트랙트를 시행하는 경우의 실무적 고려사항, https://github.com/Kwangkee/FL/blob/main/BCFL%40Korea.md#%EB%B6%80%EA%B2%BD%EB%8C%80

#### 실습 (TA)
- [발표] BC 리뷰
- [실습] Ethereum Simulator, Solidity
#### 학생 발표
- [학생 발표] Deep dive 주제 (응용 및 Open Challenges) 발표 : 1 page proposal

## 8주
#### 강의 (Instructor)  
- 블록체인 융합 연합학습, https://github.com/Kwangkee/FL/blob/main/BCFL%40Korea.md
  >[Recommend] [[Towards Trustworthy AI: Blockchain-based Architecture Design for Accountability and Fairness of Federated Learning Systems](https://github.com/Kwangkee/FL/blob/main/FL%40CSIRO.md#towards-trustworthy-ai)], https://scholar.google.com/citations?view_op=view_citation&hl=ko&user=TuL21poAAAAJ&sortby=pubdate&citation_for_view=TuL21poAAAAJ:koF6b02d8EEC
  >[Recommend] https://github.com/Kwangkee/FL/blob/main/BCFL%40Korea.md#%EC%84%9C%EC%9A%B8%EB%8C%80

#### 실습 (TA)
- [발표] BCFL 리뷰
- [실습] 2CP Simulator
#### 학생 발표
- [학생 발표] Deep dive 주제 (응용 및 Open Challenges) 발표 : 1 page proposal

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

