# 🚀 Deployment Guide

This guide will help you deploy your Voicemail Summarizer to the internet.

## 📋 Prerequisites

1. **Git repository**: Your code should be in a Git repository (GitHub, GitLab, etc.)
2. **OpenAI API key**: Make sure you have a valid OpenAI API key
3. **Account on deployment platform**: Choose one of the platforms below

## 🎯 Recommended: Railway Deployment

Railway is the easiest option with a generous free tier.

### Step 1: Prepare Your Repository

1. **Push your code to GitHub**:
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
   git push -u origin main
   ```

### Step 2: Deploy to Railway

1. **Go to [Railway.app](https://railway.app)**
2. **Sign up/Login** with your GitHub account
3. **Click "New Project"**
4. **Select "Deploy from GitHub repo"**
5. **Choose your repository**
6. **Railway will automatically detect it's a Python app**

### Step 3: Configure Environment Variables

1. **Go to your project dashboard**
2. **Click on "Variables" tab**
3. **Add these environment variables**:
   ```
   OPENAI_API_KEY=your_actual_openai_api_key_here
   SECRET_KEY=8df1566fd6b49a000171a1704415b839f3bffdddfb61ab09996d1a61d6f540f9
   ```

### Step 4: Deploy

1. **Railway will automatically deploy your app**
2. **Wait for deployment to complete**
3. **Click on the generated URL to access your app**

## 🌐 Alternative: Render Deployment

### Step 1: Prepare Repository (same as above)

### Step 2: Deploy to Render

1. **Go to [Render.com](https://render.com)**
2. **Sign up/Login** with your GitHub account
3. **Click "New +" → "Web Service"**
4. **Connect your GitHub repository**
5. **Configure the service**:
   - **Name**: `voicemail-summarizer`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`

### Step 3: Add Environment Variables

1. **Go to "Environment" tab**
2. **Add variables**:
   ```
   OPENAI_API_KEY=your_actual_openai_api_key_here
   SECRET_KEY=8df1566fd6b49a000171a1704415b839f3bffdddfb61ab09996d1a61d6f540f9
   ```

### Step 4: Deploy

1. **Click "Create Web Service"**
2. **Wait for deployment**
3. **Access your app via the provided URL**

## 🐳 Alternative: Heroku Deployment

### Step 1: Install Heroku CLI

```bash
# Windows (using winget)
winget install --id=Heroku.HerokuCLI

# Or download from: https://devcenter.heroku.com/articles/heroku-cli
```

### Step 2: Login and Deploy

```bash
# Login to Heroku
heroku login

# Create Heroku app
heroku create your-app-name

# Add environment variables
heroku config:set OPENAI_API_KEY=your_actual_openai_api_key_here
heroku config:set SECRET_KEY=8df1566fd6b49a000171a1704415b839f3bffdddfb61ab09996d1a61d6f540f9

# Deploy
git push heroku main

# Open the app
heroku open
```

## 🔧 Environment Variables Explained

### Required Variables

- **`OPENAI_API_KEY`**: Your OpenAI API key (get from [platform.openai.com](https://platform.openai.com/api-keys))
- **`SECRET_KEY`**: Flask secret key for session management (use the one generated earlier)

### Optional Variables

- **`PORT`**: Port number (usually set automatically by the platform)
- **`FLASK_ENV`**: Set to `production` for production deployment

## 🛡️ Security Considerations

### For Production Deployment

1. **Use HTTPS**: All platforms above provide HTTPS automatically
2. **Secure API Keys**: Never commit API keys to your repository
3. **Rate Limiting**: Consider adding rate limiting for production use
4. **File Size Limits**: The app limits uploads to 50MB
5. **Input Validation**: The app validates file types and content

### Additional Security Measures

You can add these to your `app.py` for enhanced security:

```python
# Add rate limiting
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# Add CORS protection
from flask_cors import CORS
CORS(app, origins=['https://yourdomain.com'])
```

## 📊 Monitoring and Logs

### Railway
- **Logs**: Available in the Railway dashboard
- **Metrics**: Built-in monitoring

### Render
- **Logs**: Available in the Render dashboard
- **Health checks**: Automatic health monitoring

### Heroku
- **Logs**: `heroku logs --tail`
- **Monitoring**: Heroku add-ons for monitoring

## 🔄 Updating Your Deployment

### For Railway/Render
1. **Push changes to GitHub**
2. **Deployment happens automatically**

### For Heroku
```bash
git add .
git commit -m "Update message"
git push heroku main
```

## 💰 Cost Considerations

### Railway
- **Free tier**: $5 credit monthly
- **Paid**: Pay-as-you-use

### Render
- **Free tier**: Available with limitations
- **Paid**: Starting at $7/month

### Heroku
- **Free tier**: Discontinued
- **Paid**: Starting at $7/month

## 🆘 Troubleshooting

### Common Issues

1. **"Build failed"**
   - Check that all dependencies are in `requirements.txt`
   - Ensure Python version is compatible

2. **"Environment variables not found"**
   - Double-check variable names
   - Ensure no extra spaces in values

3. **"OpenAI API errors"**
   - Verify API key is correct
   - Check OpenAI account billing

4. **"File upload issues"**
   - Check file size limits
   - Verify file format support

### Getting Help

- **Railway**: [Discord community](https://discord.gg/railway)
- **Render**: [Documentation](https://render.com/docs)
- **Heroku**: [Support](https://help.heroku.com)

## 🎉 Success!

Once deployed, your voicemail summarizer will be available at a public URL that you can share with others!

**Example URLs**:
- Railway: `https://your-app-name.railway.app`
- Render: `https://your-app-name.onrender.com`
- Heroku: `https://your-app-name.herokuapp.com` 