# interface between rabbitmq msgs and websocket 


import sys 
import pika 
import uwsgi 

def application(env, start_response):
    """ websocket sever """
    connection = pika.BlockingConnection(
        pika.ConnectionParameter("host", "localhost")

    )
    channel = connection.channel()

    exchange = env['PATH_INFO'].replace('/', '')
    channel.exchange_declare(
        exchange=exchange, exchange_type = 'fanout'
    )

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name= result.method.queue
    
    channel.queue_bind(exchange=exchange , queue=queue_name)

    uwsgi.websocket_handshake(env['HTPP_SEC_WEBSOCKET_KEY'], env.get('HTTP_ORIGIN'))

    
    def maintain_connection():
        """ maintain websocket connection alive """
        print("Hello ahmed ...")
        try:
            uwsgi.websocket_recv_nb()
            connection.add_timeout(30, maintain_connection)
        except OSError as error:
            print(error)
            sys.exit(1)
    
    maintain_connection()

    while True:
        for method_frame, _, body in channel.consume(queue_name):
            try:
                uwsgi.websocket_send(body)
            except OSError as error:
                ptint(error)
                sys.exit(1)
            else:
                channel.basic_ack(method_frame.delivery_tag)
                    