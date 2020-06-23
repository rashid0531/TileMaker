from CommandLineParser import StartApplication

if __name__ == '__main__':
    StartApplication.start()

'''
140, 182	1052, 182
140, 630	1052, 630

python __main__.py -ip "frame000700.jpg" -ts 224,224 -sp "./here" -corA 140,182 -corB 1052,182 -corC 1052,630 -corD 140,630

Todo:
1. Build a single core version.
2. Create a logger to show the progress.
3. Build a concurrent version.

'''
