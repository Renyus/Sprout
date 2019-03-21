import importlib

from sprout import Sprout, scheduler


async def run(bot: Sprout, ctx, cmd, arg) -> None:
    if arg == 'start':
        run_all_tasks(bot)
        await bot.send(ctx, '已启动所有计划任务')
    elif arg == 'stop':
        stop_all_tasks()
        await bot.send(ctx, '已停止所有计划任务')

def run_all_tasks(bot: Sprout):
    run_vtb_notification(bot)


def run_vtb_notification(bot: Sprout):
    schedule_module = importlib.import_module('sprout.schedules.vtb_subscribe')
    scheduler.add_job(
        schedule_module.initialize,
        id='vtb_subscribe',
        kwargs={'bot': bot},
        trigger='interval',
        replace_existing=True,
        minutes=1,
    )
def stop_all_tasks():
    jobs = scheduler.get_jobs()
    for job in jobs:
        job.remove()