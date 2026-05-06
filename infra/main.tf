terraform {
  required_version = ">= 1.5.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_s3_bucket" "dataops_bucket" {
  bucket = var.bucket_name

  tags = {
    Project     = "dataops-amazon-sales"
    Environment = "academic"
    ManagedBy   = "terraform"
  }
}

resource "aws_s3_bucket_versioning" "dataops_bucket_versioning" {
  bucket = aws_s3_bucket.dataops_bucket.id

  versioning_configuration {
    status = "Enabled"
  }
}