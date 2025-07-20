# Financial Chatbot with Real-Time Data

A comprehensive financial chatbot application that provides real-time financial data, AI-powered advice, and product comparisons using live market data from the internet.

## 🚀 Features

### Real-Time Data Sources
- **Stock Market Data**: Live prices and changes for major stocks (AAPL, GOOGL, MSFT, TSLA, AMZN)
- **Cryptocurrency Data**: Real-time crypto prices and market movements (BTC, ETH, USDT, BNB)
- **Bank Rates**: Current interest rates from major banks (Chase, Bank of America, Wells Fargo, Ally)
- **Federal Funds Rate**: Live Federal Reserve rate data
- **Market Summary**: Comprehensive market overview with timestamps

### AI-Powered Financial Advisor
- **Contextual Responses**: AI provides advice based on current market conditions
- **Product Comparisons**: Intelligent comparison of financial products
- **Risk Assessment**: Built-in risk considerations in recommendations
- **Personalized Guidance**: Tailored financial advice based on user queries

### Interactive Interface
- **Tabbed Interface**: Separate tabs for banks, stocks, crypto, and market summary
- **Real-Time Updates**: Data refreshes automatically every 5 minutes
- **Visual Indicators**: Color-coded price changes (green for gains, red for losses)
- **Responsive Design**: Clean, modern UI with easy navigation

## 🛠️ Technology Stack

### Backend
- **Flask**: Python web framework
- **yfinance**: Yahoo Finance API for stock and crypto data
- **BeautifulSoup**: Web scraping capabilities
- **Groq API**: AI-powered financial advice
- **Caching**: 5-minute cache for optimal performance

### Frontend
- **React 18**: Modern React with hooks
- **Vite**: Fast build tool and dev server
- **Axios**: HTTP client for API calls
- **Real-time Updates**: Automatic data refresh

## 📦 Installation

### Prerequisites
- Python 3.8+
- Node.js 16+
- npm or yarn

### Backend Setup
```bash
cd backend
pip install -r requirements.txt
```

### Frontend Setup
```bash
cd frontend
npm install
```

## 🚀 Running the Application

### Start Backend Server
```bash
cd backend
python app.py
```
The backend will run on `http://localhost:5000`

### Start Frontend Development Server
```bash
cd frontend
npm run dev
```
The frontend will run on `http://localhost:5173`

## 📊 API Endpoints

### Chat Endpoints
- `POST /chat` - Send messages to AI financial advisor
- `GET /products` - Get comprehensive financial data
- `GET /stocks` - Get current stock market data
- `GET /crypto` - Get cryptocurrency data
- `GET /rates` - Get bank rates and federal funds rate
- `GET /market-summary` - Get market overview

## 🔧 Configuration

### API Keys
The application uses the following APIs:
- **Groq API**: For AI financial advice (configured in `groq_client.py`)
- **FRED API**: For Federal Reserve data (using demo key)
- **Yahoo Finance**: For stock and crypto data (no key required)

### Environment Variables
For production, consider setting:
- `GROQ_API_KEY`: Your Groq API key
- `FRED_API_KEY`: Your FRED API key for more reliable data

## 📈 Data Sources

### Real-Time Financial Data
1. **Stock Market**: Yahoo Finance API
2. **Cryptocurrency**: Yahoo Finance API
3. **Federal Funds Rate**: FRED (Federal Reserve Economic Data)
4. **Bank Rates**: Generated based on current market conditions

### Data Refresh
- **Cache Duration**: 5 minutes
- **Automatic Updates**: Background refresh every 5 minutes
- **Manual Refresh**: Available through tab navigation

## 🎯 Usage Examples

### Chat with AI Advisor
Ask questions like:
- "What's the best savings account rate right now?"
- "How is Apple stock performing today?"
- "Should I invest in Bitcoin?"
- "Compare CD rates from different banks"
- "What's the impact of the Federal Reserve rate on my investments?"

### View Real-Time Data
- **Bank Rates Tab**: Compare savings accounts and CDs
- **Stocks Tab**: Monitor major stock prices and changes
- **Crypto Tab**: Track cryptocurrency market movements
- **Summary Tab**: Get market overview and key metrics

## 🔒 Security Considerations

### Current Implementation
- API keys are hardcoded (not recommended for production)
- No authentication required
- CORS enabled for local development

### Production Recommendations
- Move API keys to environment variables
- Implement user authentication
- Add rate limiting
- Use HTTPS in production
- Implement proper error handling

## 🐛 Troubleshooting

### Common Issues
1. **Data not loading**: Check internet connection and API availability
2. **Chat not responding**: Verify Groq API key is valid
3. **Frontend not connecting**: Ensure backend is running on port 5000

### Error Handling
- Graceful fallbacks for API failures
- Loading states for better UX
- Console logging for debugging

## 📝 Future Enhancements

### Planned Features
- User authentication and profiles
- Portfolio tracking
- Historical data analysis
- More financial products (bonds, ETFs)
- Mobile app version
- Advanced charting and analytics

### Technical Improvements
- Database integration for user data
- WebSocket for real-time updates
- Advanced caching strategies
- API rate limiting
- Comprehensive error handling

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is open source and available under the MIT License.

## ⚠️ Disclaimer

This application is for educational and informational purposes only. It does not constitute financial advice. Always consult with a qualified financial advisor before making investment decisions. The data provided may not be real-time or accurate, and should not be used as the sole basis for financial decisions. 