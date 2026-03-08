from apscheduler.schedulers.blocking import BlockingScheduler
from main import run_pipeline

scheduler = BlockingScheduler()

scheduler.add_job(
    run_pipeline,
    trigger='cron',
    hour=0,
    minute=0,
    id='movie_pipeline'
)

print("Scheduler started - pipeline will run every night at midnight")
print("Press Ctrl+C to stop")

try:
    scheduler.start()
except KeyboardInterrupt:
    print("Scheduler stopped")
    scheduler.shutdown()