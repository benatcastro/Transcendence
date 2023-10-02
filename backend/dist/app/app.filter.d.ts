import { ArgumentsHost, ExceptionFilter } from '@nestjs/common';
export declare class AppFilter<T> implements ExceptionFilter {
    catch(exception: T, host: ArgumentsHost): void;
}
