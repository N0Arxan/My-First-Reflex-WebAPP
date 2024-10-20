"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    i = 0
    
    def inc(self):
        self.i += 1
        
    
    def dec(self):
        self.i -=1
        

def bemoola() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        
        rx.vstack(
            rx.heading("Arxan first reflex webAPP", size="9"),
            rx.button("inc",on_click=State.inc,size="4"),
            rx.text(
                State.i,
                size="9",
                color_scheme="red",
            ),
            rx.button("dec",on_click=State.dec , size="4"),
            spacing="5",
            justify="center",
            min_height="85vh",
        
        ),
        
    )


app = rx.App()
app.add_page(bemoola , route="/bemoola")
