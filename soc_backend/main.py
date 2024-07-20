from flask import Flask, request, jsonify
import pandas as pd
from data_fetch import download_historical_data
from flask_cors import CORS
from nifty_data import nifty_data
from post import post_trade_analysis
from editor import strategy_build 
from advanced import forecast 
import subprocess
import sys
import traceback
import io



app = Flask(__name__)
CORS(app)

@app.route('/', methods=['POST' , 'GET'])
def login():
    return " this is login page"

@app.route('/get_stock_data', methods=['POST'])
def get_stock_data():
    data = request.json

    symbol = data.get('symbol')
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    # Download historical data
    df = download_historical_data(symbol, start_date, end_date)
    
    result = df.to_dict(orient='records')

    return jsonify(result)

@app.route('/nifty_stock', methods=['POST'])
def get_stock():
    data = request.json
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    # nifty 50 data 
    df = nifty_data(start_date, end_date)
    
    result = df.to_dict(orient='records')

    return jsonify(result)



@app.route('/stock_trend', methods=['POST'])
def stock_trend():
    data = request.json
    symbol = data.get('symbol')
    start_date = data.get('start_date')
    end_date = data.get('end_date')

    # nifty 50 data 
    df = strategy_build(symbol, start_date, end_date)
    
    result = df.to_dict(orient='records')

    return jsonify(result)



@app.route('/post_trade_analysis', methods=['POST'])
def post_trade_result():
    data = request.json
    symbol = data.get('symbol')
    start_date = data.get('start_date')
    end_date = data.get('end_date')
    df = post_trade_analysis(symbol, start_date, end_date)
    
    result = df.to_dict(orient='records')
    return jsonify(result)




@app.route('/run_strategy', methods=['POST'])
def run_strategy():
    data = request.json
    script = data.get('script', '')
    stock_data = data.get('stock_data', [])

    # Convert stock_data to a DataFrame
    df = pd.DataFrame(stock_data)

    # Save DataFrame to a buffer
    buffer = io.StringIO()
    df.to_csv(buffer, index=False)
    buffer.seek(0)

    # Save the script to a temporary file
    script_file = 'temp_script.py'
    with open(script_file, 'w') as file:
        file.write(script)

    try:
        # Prepare the input data for the script
        input_data = buffer.getvalue()

        # Run the Python script with the CSV buffer as input
        result = subprocess.run(
            ['python', script_file],
            input=input_data,
            text=True,
            capture_output=True
        )
        
        output = result.stdout
        errors = result.stderr

        return jsonify({
            'output': output if output else 'No output',
            'errors': errors if errors else 'No errors'
        })
    except Exception as e:
        return jsonify({'output': 'Error', 'errors': str(e)}), 500
    finally:
        # Clean up temporary script file
        try:
            os.remove(script_file)
        except Exception as e:
            print(f'Error removing temp file: {e}')

@app.route('/guess', methods=['POST'])
def guess():
    data = request.get_json()
    symbol = data['symbol']
    start_date = data['start_date']
    end_date = data['end_date']
    
    try:
        forecast_data = forecast(symbol, start_date, end_date)
        return jsonify(forecast_data)
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True )  
