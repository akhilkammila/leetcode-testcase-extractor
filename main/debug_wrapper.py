import time

class DebugWrapper:
    def __init__(self, wrapped_class):
        self.wrapped = wrapped_class

    # Instead of getting the actual method, we wrap the method with our own
    def __getattr__(self, attr):
        original_method = getattr(self.wrapped, attr)

        if callable(original_method):
            return self.wrap_method(original_method)
        
        return original_method

    def wrap_method(self, method):
        def time_and_screenshot_wrapper(*args, **kwards):
            # Run and print time elapsed
            print("Running method: {}".format(method.__name__))
            start = time.time()
            result = method(*args, **kwards)
            end = time.time()
            print("Time elapsed: {}".format(end - start) + "\n")

            # Take screenshot
            screenshotMethod = getattr(self.wrapped, "screenshot")
            screenshotMethod("{}.png".format(method.__name__))

            return result

        return time_and_screenshot_wrapper