# import cv2
# import cvlib as cv
# from cvlib.object_detection import draw_bbox
# from gtts import gTTS
# import playsound
# import ctypes

# def get_screen_resolution():
#     user32 = ctypes.windll.user32
#     width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
#     return width, height

# def speak_detected_items(labels):
#     if not labels:
#         return

#     intro_phrase = "The items that are detected are "
#     items_text = intro_phrase + ", ".join(labels)

#     tts = gTTS(text=items_text, lang='en')
#     tts.save('detected_items.mp3')
#     playsound.playsound('detected_items.mp3', True)

# def detect_objects_from_image(image_path):
#     frame = cv2.imread(image_path)

#     if frame is None:
#         print(f"Error: Unable to read image at '{image_path}'")
#         return [], None

#     bbox, label, conf = cv.detect_common_objects(frame)

#     output_image = draw_bbox(frame, bbox, label, conf)

#     output_image_resized = cv2.resize(output_image, (800, 600))

#     cv2.imshow("Detected Objects", output_image_resized)
#     cv2.waitKey(0)

#     return label, conf

# def detect_objects_from_video():
#     print("Choose video source:")
#     print("1. Live video from camera")
#     print("2. Video from storage")

#     video_choice = input("Enter your choice (1 or 2): ")

#     if video_choice == "1":
#         print("Choose live video source:")
#         print("1. Live from webcam")
#         print("2. Live from DroidCam")

#         live_video_choice = input("Enter your choice (1 or 2): ")

#         if live_video_choice == "1":
#             video = cv2.VideoCapture(0)  # Open camera for live video from webcam
#         elif live_video_choice == "2":
#             video = cv2.VideoCapture(1)  # Open camera for live video from DroidCam
#         else:
#             print("Invalid choice. Using default webcam.")
#             video = cv2.VideoCapture(0)

#         video.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
#         video.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

#     elif video_choice == "2":
#         while True:
#             video_path = input("Enter the path to the video file: ").strip()
#             if video_path:
#                 break
#             else:
#                 print("Invalid path. Please try again.")

#         video = cv2.VideoCapture(video_path)

#     else:
#         print("Invalid choice. Using live video from default webcam.")
#         video = cv2.VideoCapture(0)
#         video.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
#         video.set(cv2.CAP_PROP_FRAME_HEIGHT, 600)

#     labels = []
#     screen_width, screen_height = get_screen_resolution()

#     while True:
#         ret, frame = video.read()

#         if not ret:
#             break

#         bbox, label, conf = cv.detect_common_objects(frame)

#         output_frame = draw_bbox(frame, bbox, label, conf)

#         if video_choice == "2":
#             output_frame_resized = cv2.resize(output_frame, (screen_width, screen_height))
#         else:
#             output_frame_resized = cv2.resize(output_frame, (800, 600))

#         cv2.imshow("Object Detection", output_frame_resized)

#         for item in label:
#             if item not in labels:
#                 labels.append(item)

#         if cv2.waitKey(1) & 0xFF == ord("q"):
#             break

#     video.release()
#     cv2.destroyAllWindows()

#     return labels

# if __name__ == "__main__":
#     print("Choose an option:")
#     print("1. Detect objects from an image")
#     print("2. Detect objects from a video")

#     choice = input("Enter your choice (1 or 2): ")

#     if choice == "1":
#         while True:
#             image_path = input("Enter the path to the image file: ").strip()
#             if image_path:
#                 break
#             else:
#                 print("Invalid path. Please try again.")

#         detected_labels, _ = detect_objects_from_image(image_path)
#         print("Detected items:", detected_labels)
#         speak_detected_items(detected_labels)

#     elif choice == "2":
#         detected_labels = detect_objects_from_video()
#         print("Detected items:", detected_labels)
#         speak_detected_items(detected_labels)

#     else:
#         print("Invalid choice. Please enter 1 or 2.")




# import cv2
# import cvlib as cv
# from cvlib.object_detection import draw_bbox
# from gtts import gTTS
# import playsound
# import ctypes
# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog

# def get_screen_resolution():
#     user32 = ctypes.windll.user32
#     width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
#     return width, height

# def speak_detected_items(labels):
#     if not labels:
#         return

#     intro_phrase = "The items that are detected are "
#     items_text = intro_phrase + ", ".join(labels)

#     tts = gTTS(text=items_text, lang='en')
#     tts.save('detected_items.mp3')
#     playsound.playsound('detected_items.mp3', True)

# def detect_objects_from_image(image_path):
#     frame = cv2.imread(image_path)

#     if frame is None:
#         print(f"Error: Unable to read image at '{image_path}'")
#         return [], None

#     bbox, label, conf = cv.detect_common_objects(frame)

#     output_image = draw_bbox(frame, bbox, label, conf)

#     output_image_resized = cv2.resize(output_image, (800, 600))

#     cv2.imshow("Detected Objects", output_image_resized)
#     cv2.waitKey(0)

#     return label, conf

# def start_detection_window():
#     root = tk.Tk()
#     root.title("Object Detection Software")

#     # Center the window on screen
#     screen_width, screen_height = get_screen_resolution()
#     window_width, window_height = 400, 300
#     x = (screen_width // 2) - (window_width // 2)
#     y = (screen_height // 2) - (window_height // 2)
#     root.geometry(f"{window_width}x{window_height}+{x}+{y}")

#     label = tk.Label(root, text="Welcome to our Object Detection Software", font=("Helvetica", 14))
#     label.pack(pady=20)

#     def on_enter_clicked():
#         option_window = tk.Toplevel(root)
#         option_window.title("Choose an option")

#         # Center the option window
#         option_window_width, option_window_height = 300, 200
#         option_x = (screen_width // 2) - (option_window_width // 2)
#         option_y = (screen_height // 2) - (option_window_height // 2)
#         option_window.geometry(f"{option_window_width}x{option_window_height}+{option_x}+{option_y}")

#         choice_var = tk.StringVar()

#         def on_proceed_clicked():
#             choice = choice_var.get()

#             if choice == "1":  # Detect objects from an image
#                 image_path = filedialog.askopenfilename(title="Select an image file",
#                                                          filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#                 if image_path:
#                     detected_labels, _ = detect_objects_from_image(image_path)
#                     print("Detected items:", detected_labels)
#                     speak_detected_items(detected_labels)

#             elif choice == "2":  # Detect objects from a video
#                 detected_labels = detect_objects_from_video()
#                 print("Detected items:", detected_labels)
#                 speak_detected_items(detected_labels)

#         label_option = tk.Label(option_window, text="Choose an option:")
#         label_option.pack(pady=10)

#         radio_button1 = ttk.Radiobutton(option_window, text="Detect objects from an image", value="1", variable=choice_var)
#         radio_button1.pack(pady=5, anchor='w')

#         radio_button2 = ttk.Radiobutton(option_window, text="Detect objects from a video", value="2", variable=choice_var)
#         radio_button2.pack(pady=5, anchor='w')

#         proceed_button = tk.Button(option_window, text="Proceed", command=on_proceed_clicked)
#         proceed_button.pack(pady=20)

#     enter_button = tk.Button(root, text="Enter", command=on_enter_clicked, font=("Helvetica", 12))
#     enter_button.pack(pady=20)

#     root.mainloop()

# if __name__ == "__main__":
#     start_detection_window()


# import cv2
# import cvlib as cv
# from cvlib.object_detection import draw_bbox
# from gtts import gTTS
# import playsound
# import ctypes
# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog

# def get_screen_resolution():
#     user32 = ctypes.windll.user32
#     width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
#     return width, height

# def speak_detected_items(labels):
#     if not labels:
#         return

#     intro_phrase = "The items that are detected are "
#     items_text = intro_phrase + ", ".join(labels)

#     tts = gTTS(text=items_text, lang='en')
#     tts.save('detected_items.mp3')
#     playsound.playsound('detected_items.mp3', True)

# def detect_objects_from_image(image_path):
#     frame = cv2.imread(image_path)

#     if frame is None:
#         print(f"Error: Unable to read image at '{image_path}'")
#         return [], None

#     bbox, label, conf = cv.detect_common_objects(frame)

#     output_image = draw_bbox(frame, bbox, label, conf)

#     output_image_resized = cv2.resize(output_image, (800, 600))

#     cv2.imshow("Detected Objects", output_image_resized)
#     cv2.waitKey(0)

#     return label, conf

# def start_detection_window():
#     root = tk.Tk()
#     root.title("Object Detection Software")

#     # Center the window on screen
#     screen_width, screen_height = get_screen_resolution()
#     window_width, window_height = 400, 300
#     x = (screen_width // 2) - (window_width // 2)
#     y = (screen_height // 2) - (window_height // 2)
#     root.geometry(f"{window_width}x{window_height}+{x}+{y}")

#     label = tk.Label(root, text="Welcome to our Object Detection Software", font=("Helvetica", 14))
#     label.pack(pady=20)

#     def on_enter_clicked():
#         option_window = tk.Toplevel(root)
#         option_window.title("Choose an option")

#         # Center the option window
#         option_window_width, option_window_height = 300, 200
#         option_x = (screen_width // 2) - (option_window_width // 2)
#         option_y = (screen_height // 2) - (option_window_height // 2)
#         option_window.geometry(f"{option_window_width}x{option_window_height}+{option_x}+{option_y}")

#         choice_var = tk.StringVar()

#         def on_proceed_clicked():
#             choice = choice_var.get()

#             if choice == "1":  # Detect objects from an image
#                 image_path = filedialog.askopenfilename(title="Select an image file",
#                                                          filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#                 if image_path:
#                     detected_labels, _ = detect_objects_from_image(image_path)
#                     print("Detected items:", detected_labels)
#                     speak_detected_items(detected_labels)

#             elif choice == "2":  # Detect objects from a video
#                 video_options_window = tk.Toplevel(root)
#                 video_options_window.title("Choose Video Source")

#                 video_option_label = tk.Label(video_options_window, text="Choose video source:")
#                 video_option_label.pack(pady=10)

#                 def on_video_proceed_clicked(video_choice):
#                     if video_choice == "1":  # Live video options
#                         live_video_options_window = tk.Toplevel(root)
#                         live_video_options_window.title("Choose Live Video Source")

#                         live_video_option_label = tk.Label(live_video_options_window, text="Choose live video source:")
#                         live_video_option_label.pack(pady=10)

#                         def on_live_video_proceed_clicked(live_video_choice):
#                             if live_video_choice == "1":  # Webcam
#                                 video_capture = cv2.VideoCapture(0)
#                             elif live_video_choice == "2":  # Droid
#                                 video_capture = cv2.VideoCapture(1)
#                             else:
#                                 return

#                             perform_object_detection(video_capture)

#                         radio_button3 = ttk.Radiobutton(live_video_options_window, text="Detect objects using webcam", value="1")
#                         radio_button3.pack(pady=5, anchor='w')

#                         radio_button4 = ttk.Radiobutton(live_video_options_window, text="Detect objects using Droid", value="2")
#                         radio_button4.pack(pady=5, anchor='w')

#                         proceed_button = tk.Button(live_video_options_window, text="Proceed",
#                                                    command=lambda: on_live_video_proceed_clicked(live_video_choice_var.get()))
#                         proceed_button.pack(pady=20)

#                     elif video_choice == "2":  # Stored video
#                         video_path = filedialog.askopenfilename(title="Select a video file",
#                                                                  filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])
#                         if video_path:
#                             video_capture = cv2.VideoCapture(video_path)
#                             perform_object_detection(video_capture)

#                 radio_button5 = ttk.Radiobutton(video_options_window, text="Detect objects from live video", value="1")
#                 radio_button5.pack(pady=5, anchor='w')

#                 radio_button6 = ttk.Radiobutton(video_options_window, text="Detect objects from stored video", value="2")
#                 radio_button6.pack(pady=5, anchor='w')

#                 proceed_button = tk.Button(video_options_window, text="Proceed",
#                                            command=lambda: on_video_proceed_clicked(video_choice_var.get()))
#                 proceed_button.pack(pady=20)

#         label_option = tk.Label(option_window, text="Choose an option:")
#         label_option.pack(pady=10)

#         radio_button1 = ttk.Radiobutton(option_window, text="Detect objects from an image", value="1", variable=choice_var)
#         radio_button1.pack(pady=5, anchor='w')

#         radio_button2 = ttk.Radiobutton(option_window, text="Detect objects from a video", value="2", variable=choice_var)
#         radio_button2.pack(pady=5, anchor='w')

#         proceed_button = tk.Button(option_window, text="Proceed", command=on_proceed_clicked)
#         proceed_button.pack(pady=20)

#     enter_button = tk.Button(root, text="Enter", command=on_enter_clicked, font=("Helvetica", 12))
#     enter_button.pack(pady=20)

#     root.mainloop()

# if __name__ == "__main__":
#     start_detection_window()


# import cv2
# import cvlib as cv
# from cvlib.object_detection import draw_bbox
# from gtts import gTTS
# import playsound
# import ctypes
# import tkinter as tk
# from tkinter import ttk
# from tkinter import filedialog

# def get_screen_resolution():
#     user32 = ctypes.windll.user32
#     width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
#     return width, height

# def speak_detected_items(labels):
#     if not labels:
#         return

#     intro_phrase = "The items that are detected are "
#     items_text = intro_phrase + ", ".join(labels)

#     tts = gTTS(text=items_text, lang='en')
#     tts.save('detected_items.mp3')
#     playsound.playsound('detected_items.mp3', True)

# def detect_objects_from_image(image_path):
#     frame = cv2.imread(image_path)

#     if frame is None:
#         print(f"Error: Unable to read image at '{image_path}'")
#         return [], None

#     bbox, label, conf = cv.detect_common_objects(frame)

#     output_image = draw_bbox(frame, bbox, label, conf)

#     output_image_resized = cv2.resize(output_image, (800, 600))

#     cv2.imshow("Detected Objects", output_image_resized)
#     cv2.waitKey(0)

#     return label, conf

# def perform_object_detection(video_capture):
#     detected_labels = []

#     while True:
#         ret, frame = video_capture.read()
#         if not ret:
#             break

#         bbox, label, conf = cv.detect_common_objects(frame)

#         output_image = draw_bbox(frame, bbox, label, conf)

#         cv2.imshow("Object Detection", output_image)
#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

       
#         for item in label:
#             if item not in detected_labels:
#                 detected_labels.append(item)

#     video_capture.release()
#     cv2.destroyAllWindows()

#     if detected_labels:
#         print("Detected items:", detected_labels)
#         speak_detected_items(detected_labels)
#     else:
#         print("No objects detected.")

#     return detected_labels


# def start_detection_window():
#     root = tk.Tk()
#     root.title("Object Detection Software")

   
#     screen_width, screen_height = get_screen_resolution()
#     window_width, window_height = 400, 300
#     x = (screen_width // 2) - (window_width // 2)
#     y = (screen_height // 2) - (window_height // 2)
#     root.geometry(f"{window_width}x{window_height}+{x}+{y}")

#     label = tk.Label(root, text="Welcome to our Object Detection Software", font=("Helvetica", 14))
#     label.pack(pady=20)

#     def on_enter_clicked():
#         option_window = tk.Toplevel(root)
#         option_window.title("Choose an option")

       
#         option_window_width, option_window_height = 300, 200
#         option_x = (screen_width // 2) - (option_window_width // 2)
#         option_y = (screen_height // 2) - (option_window_height // 2)
#         option_window.geometry(f"{option_window_width}x{option_window_height}+{option_x}+{option_y}")

#         choice_var = tk.StringVar()

#         def on_proceed_clicked():
#             choice = choice_var.get()

#             if choice == "1": 
#                 image_path = filedialog.askopenfilename(title="Select an image file",
#                                                          filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
#                 if image_path:
#                     detected_labels, _ = detect_objects_from_image(image_path)
#                     print("Detected items:", detected_labels)
#                     speak_detected_items(detected_labels)

#             elif choice == "2":  
#                 video_options_window = tk.Toplevel(root)
#                 video_options_window.title("Choose Video Source")

#                 video_choice_var = tk.StringVar()

#                 video_option_label = tk.Label(video_options_window, text="Choose video source:")
#                 video_option_label.pack(pady=10)

#                 def on_video_proceed_clicked():
#                     video_choice = video_choice_var.get()
#                     if video_choice == "1":  
#                         live_video_options_window = tk.Toplevel(root)
#                         live_video_options_window.title("Choose Live Video Source")

#                         live_video_choice_var = tk.StringVar()

#                         live_video_option_label = tk.Label(live_video_options_window, text="Choose live video source:")
#                         live_video_option_label.pack(pady=10)

#                         def on_live_video_proceed_clicked():
#                             live_video_choice = live_video_choice_var.get()
#                             if live_video_choice == "1":  
#                                 video_capture = cv2.VideoCapture(0)
#                             elif live_video_choice == "2":  
#                                 video_capture = cv2.VideoCapture(1)
#                             else:
#                                 return

#                             perform_object_detection(video_capture)

#                         radio_button3 = ttk.Radiobutton(live_video_options_window, text="Detect objects using webcam", value="1", variable=live_video_choice_var)
#                         radio_button3.pack(pady=5, anchor='w')

#                         radio_button4 = ttk.Radiobutton(live_video_options_window, text="Detect objects using Droid", value="2", variable=live_video_choice_var)
#                         radio_button4.pack(pady=5, anchor='w')

#                         proceed_button = tk.Button(live_video_options_window, text="Proceed", command=on_live_video_proceed_clicked)
#                         proceed_button.pack(pady=20)

#                     elif video_choice == "2":  
#                         video_path = filedialog.askopenfilename(title="Select a video file",
#                                                                  filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])
#                         if video_path:
#                             video_capture = cv2.VideoCapture(video_path)
#                             perform_object_detection(video_capture)

#                 radio_button5 = ttk.Radiobutton(video_options_window, text="Detect objects from live video", value="1", variable=video_choice_var)
#                 radio_button5.pack(pady=5, anchor='w')

#                 radio_button6 = ttk.Radiobutton(video_options_window, text="Detect objects from stored video", value="2", variable=video_choice_var)
#                 radio_button6.pack(pady=5, anchor='w')

#                 proceed_button = tk.Button(video_options_window, text="Proceed", command=on_video_proceed_clicked)
#                 proceed_button.pack(pady=20)

#         label_option = tk.Label(option_window, text="Choose an option:")
#         label_option.pack(pady=10)

#         radio_button1 = ttk.Radiobutton(option_window, text="Detect objects from an image", value="1", variable=choice_var)
#         radio_button1.pack(pady=5, anchor='w')

#         radio_button2 = ttk.Radiobutton(option_window, text="Detect objects from a video", value="2", variable=choice_var)
#         radio_button2.pack(pady=5, anchor='w')

#         proceed_button = tk.Button(option_window, text="Proceed", command=on_proceed_clicked)
#         proceed_button.pack(pady=20)

#     enter_button = tk.Button(root, text="Enter", command=on_enter_clicked, font=("Helvetica", 12))
#     enter_button.pack(pady=20)

#     root.mainloop()

# if __name__ == "__main__":
#     start_detection_window()

import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from gtts import gTTS
import playsound
import ctypes
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def get_screen_resolution():
    user32 = ctypes.windll.user32
    width, height = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    return width, height

def speak_detected_items(labels):
    if not labels:
        return

    intro_phrase = "The items that are detected are "
    items_text = intro_phrase + ", ".join(labels)

    tts = gTTS(text=items_text, lang='en')
    tts.save('detected_items.mp3')
    playsound.playsound('detected_items.mp3', True)

def detect_objects_from_image(image_path, listbox):
    frame = cv2.imread(image_path)

    if frame is None:
        print(f"Error: Unable to read image at '{image_path}'")
        return []

    bbox, label, conf = cv.detect_common_objects(frame)

    if label:
        detected_items_label = ", ".join(label)
        listbox.insert(tk.END, f"Detected items: {detected_items_label}")
        speak_detected_items(label)
    else:
        listbox.insert(tk.END, "No objects detected.")

def perform_object_detection(video_capture, listbox):
    detected_labels = []

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        bbox, label, conf = cv.detect_common_objects(frame)

        if label:
            for item in label:
                if item not in detected_labels:
                    detected_labels.append(item)
                    listbox.insert(tk.END, f"Detected: {item}")

        cv2.imshow("Object Detection", draw_bbox(frame, bbox, label, conf))

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

    if detected_labels:
        speak_detected_items(detected_labels)

def start_detection_window():
    root = tk.Tk()
    root.title("Object Detection Software")

    screen_width, screen_height = get_screen_resolution()
    window_width, window_height = 800, 600
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    label = tk.Label(root, text="Welcome to our Object Detection Software", font=("Helvetica", 14))
    label.pack(pady=20)

    listbox = tk.Listbox(root, width=80, height=20)
    listbox.pack(pady=20)

    def on_enter_clicked():
        option_window = tk.Toplevel(root)
        option_window.title("Choose an option")

        option_window_width, option_window_height = 300, 200
        option_x = (screen_width // 2) - (option_window_width // 2)
        option_y = (screen_height // 2) - (option_window_height // 2)
        option_window.geometry(f"{option_window_width}x{option_window_height}+{option_x}+{option_y}")

        choice_var = tk.StringVar()

        def on_proceed_clicked():
            choice = choice_var.get()

            if choice == "1":
                image_path = filedialog.askopenfilename(title="Select an image file",
                                                         filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
                if image_path:
                    detect_objects_from_image(image_path, listbox)

            elif choice == "2":
                video_options_window = tk.Toplevel(root)
                video_options_window.title("Choose Video Source")

                video_choice_var = tk.StringVar()

                video_option_label = tk.Label(video_options_window, text="Choose video source:")
                video_option_label.pack(pady=10)

                def on_video_proceed_clicked():
                    video_choice = video_choice_var.get()
                    if video_choice == "1":
                        live_video_options_window = tk.Toplevel(root)
                        live_video_options_window.title("Choose Live Video Source")

                        live_video_choice_var = tk.StringVar()

                        live_video_option_label = tk.Label(live_video_options_window, text="Choose live video source:")
                        live_video_option_label.pack(pady=10)

                        def on_live_video_proceed_clicked():
                            live_video_choice = live_video_choice_var.get()
                            if live_video_choice == "1":
                                video_capture = cv2.VideoCapture(0)
                            elif live_video_choice == "2":
                                video_capture = cv2.VideoCapture(1)
                            else:
                                return

                            perform_object_detection(video_capture, listbox)

                        radio_button3 = ttk.Radiobutton(live_video_options_window, text="Detect objects using webcam", value="1", variable=live_video_choice_var)
                        radio_button3.pack(pady=5, anchor='w')

                        radio_button4 = ttk.Radiobutton(live_video_options_window, text="Detect objects using Droid", value="2", variable=live_video_choice_var)
                        radio_button4.pack(pady=5, anchor='w')

                        proceed_button = tk.Button(live_video_options_window, text="Proceed", command=on_live_video_proceed_clicked)
                        proceed_button.pack(pady=20)

                    elif video_choice == "2":
                        video_path = filedialog.askopenfilename(title="Select a video file",
                                                                 filetypes=[("Video files", "*.mp4;*.avi;*.mkv")])
                        if video_path:
                            video_capture = cv2.VideoCapture(video_path)
                            perform_object_detection(video_capture, listbox)

                radio_button5 = ttk.Radiobutton(video_options_window, text="Detect objects from live video", value="1", variable=video_choice_var)
                radio_button5.pack(pady=5, anchor='w')

                radio_button6 = ttk.Radiobutton(video_options_window, text="Detect objects from stored video", value="2", variable=video_choice_var)
                radio_button6.pack(pady=5, anchor='w')

                proceed_button = tk.Button(video_options_window, text="Proceed", command=on_video_proceed_clicked)
                proceed_button.pack(pady=20)

        label_option = tk.Label(option_window, text="Choose an option:")
        label_option.pack(pady=10)

        radio_button1 = ttk.Radiobutton(option_window, text="Detect objects from an image", value="1", variable=choice_var)
        radio_button1.pack(pady=5, anchor='w')

        radio_button2 = ttk.Radiobutton(option_window, text="Detect objects from a video", value="2", variable=choice_var)
        radio_button2.pack(pady=5, anchor='w')

        proceed_button = tk.Button(option_window, text="Proceed", command=on_proceed_clicked)
        proceed_button.pack(pady=20)

    enter_button = tk.Button(root, text="Enter", command=on_enter_clicked, font=("Helvetica", 12))
    enter_button.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    start_detection_window()
