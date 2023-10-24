import { Injectable } from '@nestjs/common';
import { PrismaService } from 'src/prisma/prisma.service';

@Injectable()
export class BlockService {
    constructor(private prisma: PrismaService) {}

    async getBlockedUsers(id: number) {
        return this.prisma.user.findUnique({
            where: { id: id },
            include: { blocks: true }
        })
    }

    async block(id: number, blockId: number) {
        return this.prisma.user.update({
            where: { id: id },
            data: {
                blocks: {
                    connect: {
                        id: blockId,
                    }
                }
            }
        })
    }
    
    async unblock(id: number, blockId: number) {
        return this.prisma.user.update({
            where: { id: id },
            data: {
                blocks: {
                    disconnect: {
                        id: blockId,
                    }
                }
            }
        })
    }

}