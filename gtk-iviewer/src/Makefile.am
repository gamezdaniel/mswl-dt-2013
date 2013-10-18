## Process this file with automake to produce Makefile.in

## Created by Anjuta



AM_CPPFLAGS = \
	-DPACKAGE_LOCALE_DIR=\""$(localedir)"\" \
	-DPACKAGE_SRC_DIR=\""$(srcdir)"\" \
	-DPACKAGE_DATA_DIR=\""$(pkgdatadir)"\" \
	$(GTK_IVIEWER_CFLAGS)

AM_CFLAGS =\
	 -Wall\
	 -g

bin_PROGRAMS = gtk_iviewer

gtk_iviewer_SOURCES = \
	main.c

gtk_iviewer_LDFLAGS = \
	-Wl,--export-dynamic

gtk_iviewer_LDADD = $(GTK_IVIEWER_LIBS)


