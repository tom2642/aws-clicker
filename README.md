English | 日本語

<a name="english"></a>

Serverless Global Click Counter
A simple, fully-serverless web application that tracks and displays the number of clicks on a button from users around the world. This project is a practical demonstration of building a scalable, event-driven application on AWS using Infrastructure as Code.

Live Demo: https://www.your-custom-domain.com

Architecture
This application is built entirely on serverless AWS services, ensuring high availability, scalability, and cost-efficiency (pay-per-use). All infrastructure is defined and deployed using a single AWS CloudFormation template.

The workflow is as follows:

The user visits the static website hosted in S3 and delivered globally by CloudFront. The domain is managed by Route 53.

The frontend JavaScript makes API calls to API Gateway.

API Gateway triggers a Lambda function.

The Lambda function determines the user's country from the request IP, updates a counter in a DynamoDB table, and returns the full, updated list of country rankings.

The frontend JavaScript dynamically updates the page with the new data.

Core Features
Global Click Tracking: Counts every click on the button.

Geolocation: Determines the user's country of origin for each click.

Live Ranking: Displays a real-time, sorted leaderboard of clicks by country.

Fully Automated Deployment: All AWS resources are managed via a CloudFormation template.

Technology Stack
Frontend: HTML, CSS (Bootstrap 5), JavaScript

Backend: AWS Lambda (Python 3.12)

Database: Amazon DynamoDB (NoSQL)

API: Amazon API Gateway (HTTP API)

Hosting & CDN: Amazon S3 & Amazon CloudFront

DNS: Amazon Route 53

Security: AWS Certificate Manager (for SSL/TLS)

Infrastructure as Code: AWS CloudFormation

Project Structure
.
├── .gitignore
├── README.md
│
├── frontend/          # Static website files
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── src/               # Lambda function source code
│   └── app.py
│
├── template.yaml      # CloudFormation template for all infrastructure
└── requirements.txt   # Python dependencies for Lambda

Setup and Deployment
Follow these steps to deploy the entire stack to your own AWS account.

Prerequisites
An AWS Account.

AWS CLI installed and configured.

A registered domain name in Amazon Route 53.

Python 3.12+ and pip installed locally.

Step 1: Create an ACM Certificate (One-Time Manual Step)
A certificate is required for HTTPS. CloudFormation cannot create this for you.

Navigate to the AWS Certificate Manager (ACM) console.

IMPORTANT: Switch your region to US East (N. Virginia) us-east-1. Certificates for CloudFront must be in this region.

Request a public certificate for your custom domain (e.g., www.your-domain.com).

Follow the DNS validation steps by adding the CNAME record to your domain in Route 53.

Once the certificate status is "Issued", copy its ARN.

Step 2: Prepare the Deployment Package
First, package the Lambda function and its dependencies.

# Install Python dependencies into a temporary package directory
mkdir -p package
pip install -r requirements.txt -t ./package

# Copy your Lambda source code into the package directory
cp src/app.py ./package/

# Create the zip file from the package directory
cd package
zip -r ../function.zip .
cd ..

Step 3: Deploy the CloudFormation Stack
Deploy the entire infrastructure using the AWS CLI. Replace the placeholder values in the command below.

aws cloudformation deploy \
  --template-file template.yaml \
  --stack-name serverless-clicker-stack \
  --parameter-overrides \
    DomainName=[www.your-domain.com](https://www.your-domain.com) \
    CertificateArn=arn:aws:acm:us-east-1:123456789012:certificate/your-cert-id \
  --capabilities CAPABILITY_IAM

DomainName: Your full custom domain name.

CertificateArn: The ARN of the ACM certificate you created in Step 1.

Step 4: Upload Frontend Files
After the stack is created, CloudFormation will create the S3 bucket. You need to upload your frontend files to it.

aws s3 sync ./frontend s3://[www.your-domain.com](https://www.your-domain.com)

Your website is now live! It may take a few minutes for the CloudFront distribution and DNS records to fully propagate.

<a name="japanese"></a>

サーバーレス・グローバル・クリックカウンター (日本語)
世界中のユーザーからのクリックを記録するシンプルな完全サーバーレスのWebアプリケーションです。このプロジェクトは、Infrastructure as Code (IaC) を使用して、イベント駆動型アプリをAWS上に構築する実践的なデモンストレーションです。

ライブデモ: https://www.your-custom-domain.com

アーキテクチャ
このアプリケーションは、AWSのサーバーレスサービスのみで構築されており、高い可用性、スケーラビリティ、およびコスト効率（従量課金制）を実現しています。すべてのインフラは、単一のAWS CloudFormationテンプレートによって定義およびデプロイされます。

ワークフローは以下の通りです：

ユーザーは、S3でホストされ、CloudFrontによってグローバルに配信される静的ウェブサイトにアクセスします。ドメインはRoute 53で管理されます。

フロントエンドのJavaScriptがAPI GatewayにAPIコールを行います。

API GatewayがLambda関数をトリガーします。

Lambda関数は、リクエストIPからユーザーの国を特定し、DynamoDBテーブルのカウンターを更新し、更新された国別ランキングの完全なリストを返します。

フロントエンドのJavaScriptが、新しいデータでページを動的に更新します。

主な機能
グローバルクリック追跡: すべてのクリックのカウント

ジオロケーション: ユーザーの国の特定

ライブランキング: ソートした国別のクリックランキングのリアルタイム表示

完全自動デプロイ: すべてのAWSリソースはCloudFormationテンプレートで管理される

技術スタック
フロントエンド: HTML, CSS (Bootstrap 5), JavaScript

バックエンド: AWS Lambda (Python 3.12)

データベース: Amazon DynamoDB (NoSQL)

API: Amazon API Gateway (HTTP API)

ホスティング & CDN: Amazon S3 & Amazon CloudFront

DNS: Amazon Route 53

セキュリティ: AWS Certificate Manager (SSL/TLS用)

Infrastructure as Code: AWS CloudFormation

セットアップとデプロイ
（セットアップとデプロイの手順は、技術的な用語が多いため、オリジナルの英語のセクションをご参照ください。）