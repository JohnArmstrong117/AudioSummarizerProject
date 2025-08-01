# 🎤 Voicemail Summarizer

A modern web application that automatically transcribes voicemail audio files and generates intelligent summaries while preserving all critical information.

🌐 **Live Demo**: [https://web-production-beef.up.railway.app/](https://web-production-beef.up.railway.app/)

## ✨ Features

- **Audio Transcription**: Converts audio files to text using OpenAI's Whisper API
- **Intelligent Summarization**: Creates concise summaries using GPT-3.5-turbo
- **Critical Information Preservation**: Ensures important details like names, contact info, deadlines, and action items are maintained
- **Modern Web Interface**: Beautiful, responsive design with drag-and-drop file upload
- **Multiple Audio Formats**: Supports MP3, WAV, M4A, OGG, FLAC, and AAC files
- **Real-time Processing**: Live status updates during transcription and summarization

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- OpenAI API key (get one at [platform.openai.com](https://platform.openai.com/api-keys))

### Installation

1. **Clone or download this project**
   ```bash
   git clone <repository-url>
   cd voicemail-summarizer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   - Copy `env_example.txt` to `.env`
   - Add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_actual_api_key_here
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open your browser**
   Navigate to `http://localhost:5000`

## 📁 Project Structure

```
voicemail-summarizer/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── env_example.txt        # Environment variables template
├── README.md             # This file
├── templates/
│   └── index.html        # Web interface
└── uploads/              # Temporary file storage (auto-created)
```

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the project root with the following variables:

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `SECRET_KEY`: Flask secret key (optional, auto-generated if not provided)
- `FLASK_ENV`: Set to 'development' for debug mode

### API Usage

The application uses two OpenAI APIs:
- **Whisper API**: For speech-to-text transcription
- **GPT-3.5-turbo**: For text summarization

## 💡 Usage

1. **Upload Audio**: Drag and drop or click to select an audio file
2. **Processing**: The app will transcribe and summarize your voicemail
3. **Results**: View both the summary and full transcript

### Supported Audio Formats

- MP3
- WAV
- M4A
- OGG
- FLAC
- AAC

### File Size Limits

- Maximum file size: 50MB
- Recommended: Clear audio with minimal background noise

## 🎯 How It Works

1. **Audio Upload**: User uploads an audio file through the web interface
2. **Transcription**: OpenAI Whisper API converts speech to text
3. **Summarization**: GPT-3.5-turbo creates a concise summary
4. **Critical Information Preservation**: The AI is specifically prompted to maintain:
   - Caller names and contact information
   - Urgent matters or deadlines
   - Action items or requests
   - Important dates, times, or numbers
   - Business-related details

## 🔒 Security & Privacy

- Audio files are temporarily stored and automatically deleted after processing
- No data is permanently stored on the server
- All API calls are made directly to OpenAI's secure endpoints
- HTTPS is recommended for production deployment

## 🚀 Deployment

### Live Application
This application is currently deployed and live at: [https://web-production-beef.up.railway.app/](https://web-production-beef.up.railway.app/)

### Local Development
```bash
python app.py
```

### Production Deployment
For production, consider using:
- Gunicorn: `gunicorn app:app`
- Docker containerization
- Cloud platforms (Heroku, AWS, Google Cloud)

## 🛠️ Customization

### Modifying the Summary Style
Edit the system prompt in `app.py` (lines 58-67) to change how summaries are generated.

### Adding New Audio Formats
Update the `ALLOWED_EXTENSIONS` set in `app.py` to include additional file types.

### Changing API Models
Modify the model parameters in the `summarize_text()` function to use different GPT models or adjust parameters like `temperature` and `max_tokens`.

## 📊 API Endpoints

- `GET /`: Main web interface
- `POST /upload`: File upload and processing endpoint
- `GET /health`: Health check endpoint

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 🆘 Troubleshooting

### Common Issues

1. **"OpenAI API key not found"**
   - Ensure your `.env` file exists and contains the correct API key
   - Verify the API key is valid and has sufficient credits

2. **"Failed to transcribe audio"**
   - Check that the audio file is clear and contains speech
   - Ensure the file format is supported
   - Verify the file size is under 50MB

3. **"Failed to summarize text"**
   - Check your OpenAI API usage and billing
   - Ensure the transcript was generated successfully

### Getting Help

If you encounter issues:
1. Check the console logs for error messages
2. Verify your OpenAI API key and account status
3. Ensure all dependencies are installed correctly

## 🔮 Future Enhancements

Potential improvements:
- Batch processing for multiple files
- Email integration for voicemail forwarding
- Custom summary templates
- Language detection and translation
- Integration with phone systems
- Mobile app version
