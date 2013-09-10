/*
    May be compiled with:
        gcc -g -std=gnu99 -Wall -o test.bin test.c `pkg-config --cflags --libs glib-2.0 gdk-pixbuf-2.0`
*/
#include <glib.h>
#include <gdk-pixbuf/gdk-pixbuf.h>
#include <stdlib.h>

static void handle_error(GError *error) {
    if(error != NULL) {
        printf("Error %s\n", error->message);
        exit(1);
    }
}


int main (int argc, char *argv[])
{
    FILE *f;
    guint8 buffer[100000];
    gsize length;
    GdkPixbufLoader *loader;
    GdkPixbuf *pixbuf;
    GError *error = NULL;
    g_type_init();
    f = fopen ("image.jpg", "r");
    length = fread (buffer, 1, sizeof(buffer), f);
    fclose (f);
    printf("Read %d bytes.\n", length);
    
    loader = gdk_pixbuf_loader_new();
    gdk_pixbuf_loader_write (loader, buffer, length, &error);
    handle_error(error);
    pixbuf = gdk_pixbuf_loader_get_pixbuf (loader);
    printf("Image size: (%d x %d)\n", gdk_pixbuf_get_width(pixbuf), gdk_pixbuf_get_height(pixbuf));
    return 0;
}