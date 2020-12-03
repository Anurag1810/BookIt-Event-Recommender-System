from app import app
if __name__ == '__main__':
    import cProfile, pstats

    profiler = cProfile.Profile()
    profiler.enable()
    app.run(debug=True)
    profiler.disable()
    stats = pstats.Stats(profiler).sort_stats('ncalls')
    stats.print_stats()
    stats.dump_stats('stats_file.dat')