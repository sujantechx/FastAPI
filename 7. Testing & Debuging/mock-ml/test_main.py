import numpy as np
from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

clinet = TestClient(app)


def test_predict_with_moc():
    with patch('model.model.predict')as  mock_predict:
        mock_predict.return_value = [99]
        response=clinet.post(
            '/predict',
            json={
                'SepalLengthCm':5.2,
                'SepalWidthCm':3.50,
                'PetalLengthCm':2.4,
                'PetalWidthCm':4.2
            }
        )
        
        assert response.status_code==200
        assert response.json() =={'prediction':99}
        mock_predict.assert_called_once(np.array([[
            
        ]]))
        