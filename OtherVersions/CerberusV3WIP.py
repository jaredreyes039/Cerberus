#!/bin/python3

import dearpygui.dearpygui as dpg

def save_callback():
    print("Save Clicked")

dpg.create_context()
dpg.create_viewport(width=720,height=640)
dpg.setup_dearpygui()
dpg.set_theme("Gold")

with dpg.window(label="Cerberus V3",width=720,height=640):
    dpg.add_text(default_value="Welcome to Cerberus V3", color=[21,230,10, 1])
    dpg.add_button(label="Save", callback=save_callback)
    dpg.add_input_text(label="string")
    dpg.add_slider_float(label="float")

dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()