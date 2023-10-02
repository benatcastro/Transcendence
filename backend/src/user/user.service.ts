import { Injectable } from '@nestjs/common';
import { PrismaService } from 'src/prisma/prisma.service';
import { Prisma, User } from '@prisma/client';

@Injectable()
export class UserService {
    constructor(private prisma: PrismaService) {}

    async all(): Promise<User[]> {
        return this.prisma.user.findMany();
    }

    async create(data: Prisma.UserCreateInput): Promise<User> {
        return this.prisma.user.create({ data });
    }

    async updateEmailById(req_id: number, newEmail: string) {
        return this.prisma.user.update({
            where: { id: req_id },
            data: { email: newEmail },
        });
    }
}
