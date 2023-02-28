# from dash import dash, html, dcc
import plotly.graph_objs as go
import numpy as np

def plot3D(matriksOfPoint, n, result):

        x = [matriksOfPoint[i][0] for i in range(n)]
        y = [matriksOfPoint[i][1] for i in range(n)]
        z = [matriksOfPoint[i][2] for i in range(n)]

        # create a 3D scatter plot
        fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(
                size=5,
                color='blue',
                colorscale='Viridis',
                opacity=0.8
        ))])

        fig.add_trace(go.Scatter3d(x=[result[1][0]], y=[result[1][1]], z=[result[1][2]], mode='markers', marker=dict(
                size=10,
                color='red',
                symbol='square-open'
        )))

        fig.add_trace(go.Scatter3d(x=[result[2][0]], y=[result[2][1]], z=[result[2][2]], mode='markers', marker=dict(
                size=10,
                color='red',
                symbol='square-open'
        )))

        fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))

        fig.show()

        # app = dash.Dash()
        # app.layout = html.Div([
        # dcc.Graph(figure=fig)
        # ])

        # app.run_server(debug=True, use_reloader=False) 
