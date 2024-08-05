from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

# Cargar las reglas preentrenadas
rules = pd.read_json('association_rules.json', orient='records')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    product_id = data['product_id']
    
    # Imprimir algunos valores de 'antecedents' para depuración
    print("Ejemplo de antecedents:", rules['antecedents'].head())
    
    # Verificar el tipo de datos en 'antecedents'
    print("Tipo de datos en antecedents:", type(rules['antecedents'].iloc[0]))

    # Filtrar reglas relevantes
    relevant_rules = rules[rules['antecedents'].apply(lambda x: product_id in x)]
    
    # Obtener las recomendaciones
    recommendations = []
    for _, row in relevant_rules.iterrows():
        recommendations.extend(list(row['consequents']))
    
    recommendations = list(set(recommendations))  # Eliminar duplicados

    # Imprimir recomendaciones en consola
    print("Recomendaciones para el producto {}: {}".format(product_id, recommendations))
    
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
