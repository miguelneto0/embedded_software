import rclpy
from rclpy.node import Node
from std_msgs.msg import Float64
from example_interfaces.srv import Trigger
from pacote2.srv import GetLastReadings, ClearData  # Importa os serviços definidos

class SensorSimulator(Node):
    def __init__(self):
        super().__init__('sensor_simulator')
        self.publisher_ = self.create_publisher(Float64, 'sensor_data', 10)
        self.timer = self.create_timer(1.0, self.publish_sensor_data)

        self.readings = []
        self.history = []

        # Serviços
        self.srv_clear_data = self.create_service(ClearData, 'clear_data', self.clear_data_callback)
        self.srv_get_last_readings = self.create_service(GetLastReadings, 'get_last_readings', self.get_last_readings_callback)

    def publish_sensor_data(self):
        new_reading = float(random.uniform(0, 100)) # Gera dados do sensor (número aleatório entre 0 e 100)
        self.readings.append(new_reading)

        # Média móvel das últimas 5 leituras
        if len(self.readings) > 5:
            self.readings.pop(0)  # Mantém apenas as últimas 5 leituras
        filtered_reading = sum(self.readings) / len(self.readings)

        # Publica o valor filtrado e armazena no histórico
        msg = Float64()
        msg.data = filtered_reading
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing filtered sensor data: {filtered_reading}')
        
        # Armazena no histórico e garante o limite de 64 leituras
        self.history.append(filtered_reading)
        if len(self.history) > 64:
            self.history.pop(0)

    def clear_data_callback(self, request, response):
        # Limpa o histórico de leituras
        self.history.clear()
        response.success = True
        self.get_logger().info('History cleared.')
        return response

    def get_last_readings_callback(self, request, response):
        # Retorna as últimas 64 leituras
        response.readings = self.history
        return response

def main(args=None):
    rclpy.init(args=args)
    node = SensorSimulator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()