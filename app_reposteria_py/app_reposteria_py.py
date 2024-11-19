import reflex as rx

def index() -> rx.Component:
    return rx.container(
        # Botón para cambiar el tema
        rx.color_mode.button(position="absolute", top="1rem", right="1rem"),
        
        # Contenedor principal de la página
        rx.vstack(
            # Contenedor para el título, texto y botones en la parte superior
            rx.hstack(
                # Columna de imágenes a la izquierda
                rx.vstack(
                    rx.image(
                        src="https://sacher.com.mx/media/magefan_blog/IMG_0232.jpeg",
                        alt="",
                        border_radius="lg",
                        box_shadow="md",
                        max_width="15rem",  # Tamaño ajustado para la imagen
                    ),
                    rx.image(
                        src="https://i.pinimg.com/originals/a1/ea/d4/a1ead4218c283616e38e6f2b7fe676f2.jpg",
                        alt="",
                        border_radius="lg",
                        box_shadow="md",
                        max_width="15rem",  # Tamaño ajustado para la imagen
                    ),
                    spacing="4",  # Espaciado entre las imágenes
                    align="center",  # Alineación centrada
                    margin_right="2rem",  # Espaciado entre las imágenes y el contenido de la derecha
                ),
                
                # Espaciador para centrar el título y texto
                rx.spacer(flex="1"),  # Esto asegura que el contenido se quede centrado
                
                # Contenedor para el título, texto y botones en la parte derecha
                rx.vstack(
                    # Contenedor con título y texto
                    rx.vstack(
                        # Título centrado
                        rx.heading("¡BIENVENIDOS A LA APP DE DULCES SUEÑOS!", size="2xl", color="white", text_align="center"),
                        
                        # Descripción centrada
                        rx.text(
                            "¡Prepárate para convertirte en un maestro repostero con DULCES SUEÑOS!. "
                            "Nuestra aplicación te ofrece una colección completa de recetas deliciosas y fáciles de seguir, perfectas para todos los niveles de experiencia, desde principiantes hasta expertos",
                            size="md",
                            color="black",
                            max_width="40rem",
                            text_align="center",  # Centrado del texto
                            margin_top="1rem",  # Margen superior para el texto
                        ),
                        spacing="6",  # Espaciado entre el título y el texto
                        align="center",  # Alineación centrada
                    ),
                    
                    # Botones en la parte superior derecha
                    rx.hstack(
                        # Botón "Regístrate aquí"
                        rx.link(
                            rx.button("¡Regístrate aquí!", color_scheme="green"),
                            href="https://docs.google.com/forms/d/1uReys-KGOXo6r26sU_KMbqtrNTUPksqj-N_gzl20b-s/edit",
                            is_external=True,
                        ),  
                        # Botón "Facebook" 
                        rx.link(
                            rx.button(rx.icon(tag="facebook"), color_scheme="blue"),
                            href="https://facebook.com",
                            is_external=True,
                        ),
                        # Botón "Instagram"
                        rx.link(
                            rx.button(rx.icon(tag="instagram"), color_scheme="pink"),
                            href="https://instagram.com",
                            is_external=True,
                        ),
                        spacing="4",  # Espaciado entre los botones
                        align="end",  # Alineación de los botones a la derecha
                    ),
                    
                    # Espaciado para que los botones no se peguen al contenido
                    margin_top="2rem",
                ),
                
                # Columna de imágenes a la derecha
                rx.vstack(
                    rx.image(
                        src="https://www.nosonmagdalenassoncupcakes.com/wp-content/uploads/2018/03/Monstruo-1024x768.jpg",
                        alt="",
                        border_radius="lg",
                        box_shadow="md",
                        max_width="14rem",  # Tamaño ajustado para la imagen
                    ),
                    rx.image(
                        src="https://cloudfront-us-east-1.images.arcpublishing.com/infobae/TLDB6CL4JNAVDHET2L6RWNGLZI.jpg",
                        alt="",
                        border_radius="lg",
                        box_shadow="md",
                        max_width="14rem",  # Tamaño ajustado para la imagen
                    ),
                    spacing="4",  # Espaciado entre las imágenes
                    align="center",  # Alineación centrada
                    margin_left="2rem",  # Espaciado entre las imágenes y el contenido de la izquierda
                ),
                
                spacing="6",  # Espaciado general entre las columnas
                justify="space-between",  # Distribución equitativa de espacio entre las columnas
                align="center",  # Alineación centrada entre las columnas
            ),
            
            # Fondo y padding de la página
            bg="#ff85f3",  # Fondo rosado
            padding="2rem",
            min_height="100vh",  # Asegura que la página ocupe toda la altura de la pantalla
        ),
    )


# Crear la aplicación
app = rx.App()
app.add_page(index)