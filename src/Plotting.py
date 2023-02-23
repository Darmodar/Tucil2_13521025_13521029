import plotly.graph_objs as go
import numpy as np

x = [1,2,3,4,5,6,7,8,9,10]
y = [1,2,3,4,5,6,7,8,9,10]
z = [1,2,3,4,5,6,7,8,9,10]

# create a 3D scatter plot
fig = go.Figure(data=[go.Scatter3d(x=x, y=y, z=z, mode='markers', marker=dict(
        size=5,
        color=z,
        colorscale='Viridis',
        opacity=0.8
))])

fig.add_trace(go.Scatter3d(x=[10], y=[10], z=[10], mode='markers', marker=dict(
        size=10,
        color='red',
        symbol='square-open'
)))

fig.update_layout(scene=dict(xaxis_title='X', yaxis_title='Y', zaxis_title='Z'))
fig.show()