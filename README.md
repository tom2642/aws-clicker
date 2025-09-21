# AWS Clicker - A Serverless Learning Project

[English](#english) | [日本語](#日本語)

---

<a name="english"></a>

## 🇬🇧 English

This project is a simple, serverless web application built entirely on AWS. It's designed to track user clicks from around the world and display a real-time leaderboard.

### Purpose

As someone transitioning into a cloud and software engineering career, I created this project to gain hands-on experience with core cloud concepts. My goal was to understand how to build, deploy, and manage a full-stack application using modern, serverless technologies and Infrastructure as Code (IaC).

### Live Demo

You can try the application live here: **[https://thebuttondoesnothing.click](https://thebuttondoesnothing.click)**

### Architecture & Tech Stack

This application is 100% serverless and defined using Infrastructure as Code (AWS CloudFormation).

![Architecture Diagram](https://github.com/tom2642/aws-clicker/blob/77c59c2e93107f52ceabc78f1f81e150158ac5a6/aws-clicker-architecture.png)

**Request Flow:**
1.  A user visits the website, which is hosted in an **S3 bucket** and delivered globally via **CloudFront**. DNS is managed by **Route 53**.
2.  The frontend (JavaScript) makes a GET request to **API Gateway** to fetch the initial click counts.
3.  When the user clicks the button, a POST request is sent to **API Gateway**.
4.  API Gateway triggers a **Lambda function** (Python).
5.  The Lambda function identifies the user's country from their IP address and increments the corresponding count in a **DynamoDB** table.
6.  The function then retrieves the updated leaderboard from DynamoDB and returns it to the user.
7.  All infrastructure is managed as code using **AWS CloudFormation**. Logs are sent to **CloudWatch**.

**Services Used:**
- **Frontend:**
    - **S3:** Hosts the static website (HTML, CSS, JS).
    - **CloudFront:** Acts as a CDN for fast global delivery and provides HTTPS via **AWS Certificate Manager (ACM)**.
    - **Route 53:** Manages the custom domain name.
- **Backend:**
    - **Lambda:** Serverless compute for running the application logic in Python.
    - **API Gateway:** Provides a RESTful API endpoint for the frontend to communicate with the Lambda function.
    - **DynamoDB:** A NoSQL database to store and retrieve click counts for each country.
- **DevOps & Infrastructure:**
    - **CloudFormation:** Defines all AWS resources as code (IaC), enabling automated and repeatable deployments.
    - **IAM:** Manages permissions for AWS services to interact securely.
    - **CloudWatch:** Collects logs for monitoring and debugging.

---

<a name="日本語"></a>

## 🇯🇵 日本語

このプロジェクトは、AWS上に構築されたシンプルなサーバーレス・ウェブアプリケーションです。世界中のユーザーからのクリックを記録し、リアルタイムでランキングを表示します。

### 目的

クラウド/ソフトウェアエンジニアへのキャリアチェンジを目指しており、主要なクラウドの概念を実践的に学ぶためにこのプロジェクトを作成しました。モダンなサーバーレス技術とInfrastructure as Code (IaC) を用いて、フルスタックアプリケーションの構築、デプロイ、管理の方法を理解することが目標でした。

### ライブデモ

こちらで実際にアプリケーションを試すことができます： **[https://thebuttondoesnothing.click](https://thebuttondoesnothing.click)**

### アーキテクチャと技術スタック

このアプリケーションは100%サーバーレスで構成されており、すべてのインフラはコード（AWS CloudFormation）によって定義されています。

![アーキテクチャ図](https://github.com/tom2642/aws-clicker/blob/77c59c2e93107f52ceabc78f1f81e150158ac5a6/aws-clicker-architecture.png)

**リクエストの流れ:**
1.  ユーザーはウェブサイトにアクセスします。コンテンツは **S3バケット** にホストされ、**CloudFront** を通じてグローバルに配信されます。DNSは **Route 53** で管理されます。
2.  フロントエンド（JavaScript）は、初期表示のために **API Gateway** へGETリクエストを送信し、現在のクリック数を取得します。
3.  ユーザーがボタンをクリックすると、POSTリクエストが **API Gateway** に送信されます。
4.  API Gatewayが **Lambda関数**（Python）をトリガーします。
5.  Lambda関数は、IPアドレスからユーザーの国を特定し、**DynamoDB** テーブルの対応する国のカウントを1増やします。
6.  関数は更新されたランキングをDynamoDBから取得し、ユーザーに返します。
7.  すべてのインフラは **AWS CloudFormation** を使用してコードとして管理（IaC）されています。ログは **CloudWatch** に送られます。

**使用サービス:**
- **フロントエンド:**
    - **S3:** 静的ウェブサイト（HTML, CSS, JS）をホスティング。
    - **CloudFront:** 高速なグローバル配信のためのCDN。**AWS Certificate Manager (ACM)** によるHTTPS化も担当。
    - **Route 53:** カスタムドメインのDNS管理。
- **バックエンド:**
    - **Lambda:** アプリケーションロジックを実行するためのサーバーレス・コンピューティング環境（Python）。
    - **API Gateway:** フロントエンドがLambda関数と通信するためのRESTful APIエンドポイントを提供。
    - **DynamoDB:** 各国のクリック数を保存・取得するためのNoSQLデータベース。
- **DevOps & インフラストラクチャ:**
    - **CloudFormation:** すべてのAWSリソースをコードとして定義（IaC）。自動化され、再現可能なデプロイを実現。
    - **IAM:** AWSサービス間の安全な連携のための権限管理。
    - **CloudWatch:** モニタリングとデバッグのためのログ収集。