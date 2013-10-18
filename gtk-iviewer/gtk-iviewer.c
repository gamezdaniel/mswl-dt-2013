/*
 * gtk-iviewer.c
 * Copyright (C) 2013 dgamez <daniel.gamez@gmail.com>
 * 
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions
 * are met:
 * 1. Redistributions of source code must retain the above copyright
 *    notice, this list of conditions and the following disclaimer.
 * 2. Redistributions in binary form must reproduce the above copyright
 *    notice, this list of conditions and the following disclaimer in the
 *    documentation and/or other materials provided with the distribution.
 * 3. Neither the name ``dgamez'' nor the name of any other
 *    contributor may be used to endorse or promote products derived
 *    from this software without specific prior written permission.
 * 
 * gtk-iviewer IS PROVIDED BY dgamez ``AS IS'' AND ANY EXPRESS
 * OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
 * WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED.  IN NO EVENT SHALL dgamez OR ANY OTHER CONTRIBUTORS
 * BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
 * BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
 * WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
 * OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
 * ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 */

#include <gtk/gtk.h>
#include <glib/gi18n.h>

// Quit the application
static 
gboolean on_delete_event (GtkWidget 	*widget,
			  GdkEvent 	*event,
			  gpointer 	user_data)
{
  gtk_main_quit ();
  return GDK_EVENT_PROPAGATE;
}


// Open File Chooser Dialog to Browse for Image
static void
on_open_image (GtkButton* button, gpointer user_data)
{
	GtkWidget *image = GTK_WIDGET (user_data);
	GtkWidget *toplevel = gtk_widget_get_toplevel (image);
	GtkFileFilter *filter = gtk_file_filter_new ();
	GtkWidget *dialog = gtk_file_chooser_dialog_new (_("Browse for Image"),
	                                                 GTK_WINDOW (toplevel),
	                                                 GTK_FILE_CHOOSER_ACTION_OPEN,
	                                                 GTK_STOCK_OK, GTK_RESPONSE_ACCEPT,
	                                                 GTK_STOCK_CANCEL, GTK_RESPONSE_CANCEL,
	                                                 NULL);

	gtk_file_filter_add_pixbuf_formats (filter);
	gtk_file_chooser_add_filter (GTK_FILE_CHOOSER (dialog), filter);

	switch (gtk_dialog_run (GTK_DIALOG (dialog)))
	{
		case GTK_RESPONSE_ACCEPT:
		{
			gchar *filename = gtk_file_chooser_get_filename (GTK_FILE_CHOOSER (dialog));
			gtk_image_set_from_file (GTK_IMAGE (image), filename);
			break;
		}
		default:
			break;
	}
	gtk_widget_destroy (dialog);
}


int
main (int argc, char **argv)
{
 	GtkWidget *window, *button, *image, *box;

	gtk_init (&argc, &argv);

	// Set up the UI
	window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
	gtk_window_set_title (GTK_WINDOW (window), "gtk-iviewer");
	
	box = gtk_box_new (GTK_ORIENTATION_VERTICAL, 5);
	button = gtk_button_new_with_label (_("Browse for Image"));
	image = gtk_image_new ();
	
	gtk_box_pack_start (GTK_BOX (box), image, TRUE, TRUE, 0);
	gtk_box_pack_start (GTK_BOX (box), button, FALSE, FALSE, 0);
	
	gtk_container_add (GTK_CONTAINER (window), box);
	
	// Connect signals

	// Show open dialog when opening a file
	g_signal_connect (button, "clicked", G_CALLBACK (on_open_image), image);
	
	// Exit when the window is closed
	g_signal_connect (window, "delete-event", G_CALLBACK (on_delete_event), NULL);

	// Show objects
	gtk_widget_show (window);
	gtk_widget_show (button);
	gtk_widget_show (image);
	gtk_widget_show (box);
	
	gtk_main ();

	return 0;
}
