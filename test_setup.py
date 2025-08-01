#!/usr/bin/env python3
"""
Test script to verify the voicemail summarizer setup
"""

import os
import sys
from dotenv import load_dotenv

def test_dependencies():
    """Test if all required packages are installed"""
    print("🔍 Testing dependencies...")
    
    required_packages = [
        'flask',
        'openai', 
        'dotenv',
        'werkzeug',
        'requests'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} - NOT FOUND")
            missing_packages.append(package)
    
    if missing_packages:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        print("Please run: pip install -r requirements.txt")
        return False
    
    print("✅ All dependencies are installed!")
    return True

def test_environment():
    """Test environment configuration"""
    print("\n🔍 Testing environment configuration...")
    
    # Load .env file if it exists
    load_dotenv()
    
    # Check OpenAI API key
    api_key = os.getenv('OPENAI_API_KEY')
    if not api_key:
        print("❌ OPENAI_API_KEY not found in environment variables")
        print("Please create a .env file with your OpenAI API key")
        return False
    
    if api_key == 'your_openai_api_key_here':
        print("❌ Please replace the placeholder API key with your actual OpenAI API key")
        return False
    
    print("✅ OpenAI API key is configured")
    return True

def test_openai_connection():
    """Test OpenAI API connection"""
    print("\n🔍 Testing OpenAI API connection...")
    
    try:
        import openai
        openai.api_key = os.getenv('OPENAI_API_KEY')
        
        # Test with a simple API call
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "Hello"}],
            max_tokens=5
        )
        
        print("✅ OpenAI API connection successful")
        return True
        
    except Exception as e:
        print(f"❌ OpenAI API connection failed: {str(e)}")
        print("Please check your API key and internet connection")
        return False

def test_file_structure():
    """Test if required files exist"""
    print("\n🔍 Testing file structure...")
    
    required_files = [
        'app.py',
        'requirements.txt',
        'templates/index.html'
    ]
    
    missing_files = []
    
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - NOT FOUND")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\n❌ Missing files: {', '.join(missing_files)}")
        return False
    
    print("✅ All required files are present!")
    return True

def main():
    """Run all tests"""
    print("🚀 Voicemail Summarizer Setup Test")
    print("=" * 40)
    
    tests = [
        test_dependencies,
        test_environment,
        test_file_structure,
        test_openai_connection
    ]
    
    all_passed = True
    
    for test in tests:
        try:
            if not test():
                all_passed = False
        except Exception as e:
            print(f"❌ Test failed with error: {str(e)}")
            all_passed = False
    
    print("\n" + "=" * 40)
    
    if all_passed:
        print("🎉 All tests passed! Your setup is ready.")
        print("\nTo start the application:")
        print("1. Run: python app.py")
        print("2. Open: http://localhost:5000")
    else:
        print("❌ Some tests failed. Please fix the issues above before running the application.")
        sys.exit(1)

if __name__ == "__main__":
    main() 